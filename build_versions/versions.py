import dataclasses
import json
import logging
import re
from dataclasses import dataclass
from datetime import datetime
from functools import cmp_to_key

import requests
import semver
from bs4 import BeautifulSoup

from build_versions.settings import DEFAULT_DISTRO, DEFAULT_PLATFORMS, DISTROS, VERSIONS_PATH

todays_date = datetime.utcnow().date().isoformat()

by_semver_key = cmp_to_key(semver.compare)

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
    image: str | None = None
    distro: str | None = None


@dataclass
class NodeJsVersion(LanguageVersion):
    pass


@dataclass
class PythonVersion(LanguageVersion):
    canonical_version: str
    key: str
    image: str
    distro: str


@dataclass
class BuildVersion:
    key: str
    python: str
    python_canonical: str
    python_image: str
    nodejs: str
    nodejs_canonical: str
    distro: str
    platforms: list[str]


def _fetch_tags(package: str, page=1) -> list[str]:
    """Fetch available docker tags."""
    result = requests.get(
        f"https://registry.hub.docker.com/v2/namespaces/library/repositories/{package}/tags",
        params={"page": page, "page_size": 100},
        timeout=10.0,
    )
    result.raise_for_status()
    data = result.json()
    tags = [tag["name"] for tag in data["results"]]
    if not data["next"]:
        return tags
    return tags + _fetch_tags(package, page=page + 1)


def _latest_patch(tags: list[str], ver: str, patch_pattern: re.Pattern, distro: str):
    tags = [tag for tag in tags if tag.startswith(ver) and tag.endswith(f"-{distro}") and patch_pattern.match(tag)]
    return sorted(tags, key=by_semver_key, reverse=True)[0] if tags else ""


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


def fetch_supported_nodejs_versions() -> list[SupportedVersion]:
    """Download list of official releases, skipping unreleased and unsupported versions"""
    result = requests.get("https://raw.githubusercontent.com/nodejs/Release/master/schedule.json", timeout=10.0)
    release_schedule = result.json()

    versions = []
    for ver, detail in release_schedule.items():
        if detail["start"] <= todays_date <= detail["end"]:
            versions.append(SupportedVersion(version=ver, start=detail["start"], end=detail["end"]))

    return versions


def decide_python_versions(distros: list[str], supported_versions: list[SupportedVersion]) -> list[PythonVersion]:
    python_patch_re = "|".join([rf"^(\d+\.\d+\.\d+-{distro})$" for distro in distros])
    python_wanted_tag_pattern = re.compile(python_patch_re)

    # FIXME: can we avoid enumerating all tags to speed up things?
    logger.debug("Fetching tags for python")
    tags = [tag for tag in _fetch_tags("python") if python_wanted_tag_pattern.match(tag)]

    versions: list[PythonVersion] = []
    for supported_version in supported_versions:
        ver = supported_version.version
        for distro in distros:
            canonical_image = _latest_patch(tags, ver, python_wanted_tag_pattern, distro)
            if not canonical_image:
                logger.warning(f"Not good. ver={ver} distro={distro} not in tags, skipping...")
                continue

            versions.append(
                PythonVersion(
                    canonical_version=canonical_image.replace(f"-{distro}", ""),
                    image=canonical_image,
                    key=ver,
                    distro=distro,
                ),
            )

    return sorted(versions, key=lambda v: by_semver_key(v.canonical_version), reverse=True)


def decide_nodejs_versions(supported_versions: list[SupportedVersion]) -> list[NodeJsVersion]:
    nodejs_patch_re = rf"^(\d+\.\d+\.\d+-{DEFAULT_DISTRO})$"
    nodejs_wanted_tag_pattern = re.compile(nodejs_patch_re)

    logger.debug("Fetching tags for node")
    tags = [tag for tag in _fetch_tags("node") if nodejs_wanted_tag_pattern.match(tag)]

    versions: list[NodeJsVersion] = []
    for supported_version in supported_versions:
        ver = supported_version.version[1:]  # Remove v prefix
        canonical_image = _latest_patch(tags, ver, nodejs_wanted_tag_pattern, DEFAULT_DISTRO)
        if not canonical_image:
            logger.warning(f"Not good, ver={ver} distro={DEFAULT_DISTRO} not in tags, skipping...")
            continue

        versions.append(NodeJsVersion(canonical_version=canonical_image.replace(f"-{DEFAULT_DISTRO}", ""), key=ver))

    return sorted(versions, key=lambda v: by_semver_key(v.canonical_version), reverse=True)


def version_combinations(
    nodejs_versions: list[NodeJsVersion],
    python_versions: list[PythonVersion],
) -> list[BuildVersion]:
    versions: list[BuildVersion] = []
    for p in python_versions:
        for n in nodejs_versions:
            distro = f"-{p.distro}" if p.distro != DEFAULT_DISTRO else ""
            key = f"python{p.key}-nodejs{n.key}{distro}"
            platforms = DEFAULT_PLATFORMS
            # FIXME: Enable when:
            #  - https://github.com/nodejs/node/pull/45756 is fixed
            #  - https://github.com/nodejs/unofficial-builds adds builds for musl + arm64
            if p.distro == "alpine":
                platforms = ["linux/amd64"]
            versions.append(
                BuildVersion(
                    key=key,
                    python=p.key,
                    python_canonical=p.canonical_version,
                    python_image=p.image,
                    nodejs=n.key,
                    nodejs_canonical=n.canonical_version,
                    distro=p.distro,
                    platforms=platforms,
                ),
            )

    versions = sorted(versions, key=lambda v: DISTROS.index(v.distro))
    versions = sorted(versions, key=lambda v: by_semver_key(v.nodejs_canonical), reverse=True)
    versions = sorted(versions, key=lambda v: by_semver_key(v.python_canonical), reverse=True)
    return versions


def decide_version_combinations(
    distros: list[str],
    supported_python_versions: list[SupportedVersion],
    supported_node_versions: list[SupportedVersion],
) -> list[BuildVersion]:
    distros = list(set(distros))
    # Use the latest patch version from each minor
    python_versions = decide_python_versions(distros, supported_python_versions)
    # Use the latest minor version from each major
    nodejs_versions = decide_nodejs_versions(supported_node_versions)
    return version_combinations(nodejs_versions, python_versions)


def persist_versions(versions: list[BuildVersion], dry_run=False):
    if dry_run:
        logger.debug(versions)
        return
    with VERSIONS_PATH.open("w+") as fp:
        version_dicts = [dataclasses.asdict(version) for version in versions]
        json.dump({"versions": version_dicts}, fp, indent=2)


def load_versions() -> list[BuildVersion]:
    with VERSIONS_PATH.open() as fp:
        version_dicts = json.load(fp)["versions"]
        return [BuildVersion(**version) for version in version_dicts]


def find_new_or_updated(current_versions, versions, force=False):
    if force:
        logger.warning("Generating full build matrix because --force is set")

    current_versions = {ver["key"]: ver for ver in current_versions}
    versions = {ver["key"]: ver for ver in versions}
    new_or_updated = []

    for key, ver in versions.items():
        # does key exist and are version dicts equal?
        updated = key in current_versions and ver != current_versions[key]
        new = key not in current_versions
        if new or updated or force:
            new_or_updated.append(ver)

    return new_or_updated
