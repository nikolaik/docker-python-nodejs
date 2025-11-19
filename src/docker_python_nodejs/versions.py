import dataclasses
import datetime
import json
import logging
import re
from dataclasses import dataclass
from typing import TYPE_CHECKING

import requests
from bs4 import BeautifulSoup
from semver.version import Version

from docker_python_nodejs.readme import format_supported_versions

from .docker_hub import DockerImageDict, DockerTagDict, fetch_tags
from .nodejs_versions import (
    fetch_node_releases,
    fetch_node_unofficial_releases,
    fetch_nodejs_release_schedule,
)
from .settings import DEFAULT_DISTRO, DEFAULT_PLATFORMS, DISTROS, VERSIONS_PATH

if TYPE_CHECKING:
    from pathlib import Path

todays_date = datetime.datetime.now(datetime.UTC).date().isoformat()


logger = logging.getLogger("dpn")


@dataclass
class SupportedVersion:
    """A supported version of either Python or Node.js with start and end of support dates"""

    start: str
    end: str
    version: str


@dataclass
class LanguageVersion:
    canonical_version: str
    key: str
    distro: str


@dataclass
class NodeJsVersion(LanguageVersion):
    image: str | None = None


@dataclass
class PythonVersion(LanguageVersion):
    image: str


@dataclass
class BuildVersion:
    """A docker image build for a specific combination of python and nodejs versions"""

    key: str
    python: str
    python_canonical: str
    python_image: str
    nodejs: str
    nodejs_canonical: str
    distro: str
    platforms: list[str]
    digest: str = ""


def _is_platform_image(platform: str, image: DockerImageDict) -> bool:
    os, arch = platform.split("/")
    return os == image["os"] and arch == image["architecture"]


def _wanted_image_platforms(distro: str) -> list[str]:
    """
    Returns the supported image platforms for a distro
    FIXME: Enable linux/arm64 for alpine when:
      - https://github.com/nodejs/node/pull/45756 is fixed
      - https://github.com/nodejs/unofficial-builds adds builds for musl + arm64
    """
    if distro == "alpine":
        return ["linux/amd64"]
    return DEFAULT_PLATFORMS


def _image_tag_has_platforms(tag: DockerTagDict, distro: str) -> bool:
    for platform in _wanted_image_platforms(distro):
        has_platform = any(_is_platform_image(platform, image) for image in tag["images"])
        if not has_platform:
            return False

    return True


def _wanted_tag(tag: DockerTagDict, ver: str, distro: str) -> bool:
    return tag["name"].startswith(ver) and tag["name"].endswith(f"-{distro}") and _image_tag_has_platforms(tag, distro)


def _latest_patch(tags: list[DockerTagDict], ver: str, distro: str) -> str | None:
    tags = [tag for tag in tags if _wanted_tag(tag, ver, distro)]
    return sorted(tags, key=lambda x: Version.parse(x["name"]), reverse=True)[0]["name"] if tags else None


def scrape_supported_python_versions() -> list[SupportedVersion]:
    """Scrape supported python versions (risky)."""
    versions = []
    version_table_row_selector = "#supported-versions tbody tr"

    res = requests.get("https://devguide.python.org/versions/", timeout=10.0)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    version_table_rows = soup.select(version_table_row_selector)
    for ver in version_table_rows:
        branch, _, _, first_release, end_of_life, _ = (v.text for v in ver.find_all("td"))
        if first_release <= todays_date <= end_of_life:
            versions.append(SupportedVersion(version=branch, start=first_release, end=end_of_life))

    return versions


def decide_python_versions(distros: list[str], supported_versions: list[SupportedVersion]) -> list[PythonVersion]:
    python_patch_re = "|".join([rf"^(\d+\.\d+\.\d+-{distro})$" for distro in distros])
    python_wanted_tag_pattern = re.compile(python_patch_re)

    # FIXME: can we avoid enumerating all tags to speed up things?
    logger.debug("Fetching tags for python")
    tags = [tag for tag in fetch_tags("python") if python_wanted_tag_pattern.match(tag["name"])]

    versions: list[PythonVersion] = []
    for supported_version in supported_versions:
        ver = supported_version.version
        for distro in distros:
            canonical_image = _latest_patch(tags, ver, distro)
            platforms = _wanted_image_platforms(distro)
            if not canonical_image:
                logger.warning(
                    f"Not good. ver={ver} distro={distro} platforms={','.join(platforms)} not in tags, skipping...",
                )
                continue

            versions.append(
                PythonVersion(
                    canonical_version=canonical_image.replace(f"-{distro}", ""),
                    image=canonical_image,
                    key=ver,
                    distro=distro,
                ),
            )

    return sorted(versions, key=lambda v: Version.parse(v.canonical_version), reverse=True)


def fetch_supported_nodejs_versions() -> list[SupportedVersion]:
    release_schedule = fetch_nodejs_release_schedule()
    versions = []
    for ver, detail in release_schedule.items():
        if detail["start"] <= todays_date <= detail["end"]:
            versions.append(SupportedVersion(version=ver, start=detail["start"], end=detail["end"]))

    return versions


def supported_versions() -> tuple[list[SupportedVersion], list[SupportedVersion]]:
    supported_python_versions = scrape_supported_python_versions()
    supported_nodejs_versions = fetch_supported_nodejs_versions()
    supported_versions = format_supported_versions(supported_python_versions, supported_nodejs_versions)
    logger.debug(f"Found the following supported versions:\n{supported_versions}")
    return supported_python_versions, supported_nodejs_versions


def _has_arch_files(files: list[str], distro: str) -> bool:
    if distro == "alpine":
        return {"linux-x64-musl"}.issubset(files)
    return {"linux-arm64", "linux-x64"}.issubset(files)


def decide_nodejs_versions(distros: list[str], supported_versions: list[SupportedVersion]) -> list[NodeJsVersion]:
    logger.debug("Fetching releases for node")
    node_releases = fetch_node_releases()
    node_unofficial_releases = fetch_node_unofficial_releases()

    versions: list[NodeJsVersion] = []
    for supported_version in supported_versions:
        ver = supported_version.version[1:]  # Remove v prefix
        for distro in distros:
            distro_releases = node_unofficial_releases if distro == "alpine" else node_releases
            matching_releases = [
                rel
                for rel in distro_releases
                if rel["version"][1:].startswith(ver) and _has_arch_files(rel["files"], distro)
            ]
            latest_patch_version = (
                sorted(matching_releases, key=lambda x: Version.parse(x["version"][1:]), reverse=True)[0]["version"][1:]
                if matching_releases
                else None
            )
            if not latest_patch_version:
                logger.warning(f"Not good, ver={ver} distro={distro} not in node releases, skipping...")
                continue

            versions.append(NodeJsVersion(canonical_version=latest_patch_version, key=ver, distro=distro))

    return sorted(versions, key=lambda v: Version.parse(v.canonical_version), reverse=True)


def version_combinations(
    nodejs_versions: list[NodeJsVersion],
    python_versions: list[PythonVersion],
) -> list[BuildVersion]:
    versions: list[BuildVersion] = []
    for p in python_versions:
        for n in nodejs_versions:
            if p.distro != n.distro:
                continue

            # Skip distro in key if it's the default
            distro_key = f"-{p.distro}" if p.distro != DEFAULT_DISTRO else ""
            key = f"python{p.key}-nodejs{n.key}{distro_key}"
            versions.append(
                BuildVersion(
                    key=key,
                    python=p.key,
                    python_canonical=p.canonical_version,
                    python_image=p.image,
                    nodejs=n.key,
                    nodejs_canonical=n.canonical_version,
                    distro=p.distro,
                    platforms=_wanted_image_platforms(p.distro),
                ),
            )

    return sorted_versions(versions)


def sorted_versions(versions: list[BuildVersion]) -> list[BuildVersion]:
    versions = sorted(versions, key=lambda v: DISTROS.index(v.distro))
    versions = sorted(versions, key=lambda v: Version.parse(v.nodejs_canonical), reverse=True)
    return sorted(versions, key=lambda v: Version.parse(v.python_canonical), reverse=True)


def decide_version_combinations(
    distros: list[str],
    supported_python_versions: list[SupportedVersion],
    supported_node_versions: list[SupportedVersion],
) -> list[BuildVersion]:
    distros = list(set(distros))
    # Use the latest patch version from each minor
    python_versions = decide_python_versions(distros, supported_python_versions)
    # Use the latest minor version from each major
    nodejs_versions = decide_nodejs_versions(distros, supported_node_versions)
    return version_combinations(nodejs_versions, python_versions)


def persist_versions(versions: list[BuildVersion], dry_run: bool = False) -> None:
    if dry_run:
        logger.debug(versions)
        return
    with VERSIONS_PATH.open("w+") as fp:
        version_dicts = [dataclasses.asdict(version) for version in versions]
        json.dump({"versions": version_dicts}, fp, indent=2)


def load_versions() -> dict[str, BuildVersion]:
    with VERSIONS_PATH.open() as fp:
        versions = json.load(fp)["versions"]
        return {version["key"]: BuildVersion(**version) for version in versions}


def find_new_or_updated(
    versions: list[BuildVersion],
    current_versions: dict[str, BuildVersion],
    force: bool = False,
) -> list[BuildVersion]:
    if force:
        logger.warning("Generating full build matrix because --force is set")

    versions_dict = {ver.key: ver for ver in versions}
    new_or_updated: list[BuildVersion] = []

    for key, ver in versions_dict.items():
        current_ver = current_versions.get(key)
        if current_ver is not None:
            current_ver.digest = ""  # Ignore digest when comparing

        # does key exist and are version dicts equal?
        updated = current_ver and ver != current_ver
        new = key not in current_versions
        if new or updated or force:
            new_or_updated.append(ver)

    return new_or_updated


def load_build_contexts(builds_dir: Path) -> dict[str, BuildVersion]:
    """Find JSON files with build contexts and return the corresponding BuildVersion list"""
    logger.info(f"Loading builds metadata from {builds_dir.as_posix()}")
    versions: dict[str, BuildVersion] = {}

    for build_file in builds_dir.glob("*.json"):
        with build_file.open() as fp:
            build_data = json.load(fp)
        version = BuildVersion(**build_data)
        versions[build_data["key"]] = version

    return versions
