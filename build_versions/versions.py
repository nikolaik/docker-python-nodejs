import json
import re
from datetime import datetime
from functools import cmp_to_key

import requests
import semver
from bs4 import BeautifulSoup

from build_versions.settings import DEFAULT_DISTRO, DISTROS, VERSIONS_PATH

todays_date = datetime.utcnow().date().isoformat()


by_semver_key = cmp_to_key(semver.compare)


def _fetch_tags(package):
    # Fetch available docker tags
    result = requests.get(f"https://registry.hub.docker.com/v1/repositories/{package}/tags")
    return [r["name"] for r in result.json()]


def _latest_patch(tags, ver, patch_pattern, distro):
    tags = [tag for tag in tags if tag.startswith(ver) and tag.endswith(f"-{distro}") and patch_pattern.match(tag)]
    return sorted(tags, key=by_semver_key, reverse=True)[0] if tags else ""


def scrape_supported_python_versions():
    """Scrape supported python versions (risky)"""
    versions = []
    version_table_row_selector = "#status-of-python-branches tbody tr"

    res = requests.get("https://devguide.python.org/")
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    version_table_rows = soup.select(version_table_row_selector)
    for ver in version_table_rows:
        branch, _, _, first_release, end_of_life, _ = [v.text for v in ver.find_all("td")]
        versions.append({"version": branch, "start": first_release, "end": end_of_life})

    return versions


def fetch_supported_nodejs_versions():
    result = requests.get("https://raw.githubusercontent.com/nodejs/Release/master/schedule.json")
    return [{"version": ver, "start": detail["start"], "end": detail["end"]} for ver, detail in result.json().items()]


def decide_python_versions(distros):
    python_patch_re = "|".join([r"^(\d+\.\d+\.\d+-{})$".format(distro) for distro in distros])
    python_wanted_tag_pattern = re.compile(python_patch_re)

    tags = [tag for tag in _fetch_tags("python") if python_wanted_tag_pattern.match(tag)]
    # Skip unreleased and unsupported
    supported_versions = [v for v in scrape_supported_python_versions() if v["start"] <= todays_date <= v["end"]]

    versions = []
    for supported_version in supported_versions:
        ver = supported_version["version"]
        for distro in distros:
            canonical_image = _latest_patch(tags, ver, python_wanted_tag_pattern, distro)
            if not canonical_image:
                print(f"Not good. ver={ver} distro={distro} not in tags, skipping...")
                continue
            canonical_version = canonical_image.replace(f"-{distro}", "")
            versions.append(
                {"canonical_version": canonical_version, "image": canonical_image, "key": ver, "distro": distro}
            )

    return sorted(versions, key=lambda v: by_semver_key(v["canonical_version"]), reverse=True)


def decide_nodejs_versions():
    nodejs_patch_re = r"^(\d+\.\d+\.\d+-{})$".format(DEFAULT_DISTRO)
    nodejs_wanted_tag_pattern = re.compile(nodejs_patch_re)

    tags = [tag for tag in _fetch_tags("node") if nodejs_wanted_tag_pattern.match(tag)]
    # Skip unreleased and unsupported
    supported_versions = [v for v in fetch_supported_nodejs_versions() if v["start"] <= todays_date <= v["end"]]

    versions = []
    for supported_version in supported_versions:
        ver = supported_version["version"][1:]  # Remove v prefix
        canonical_image = _latest_patch(tags, ver, nodejs_wanted_tag_pattern, DEFAULT_DISTRO)
        if not canonical_image:
            print(f"Not good, ver={ver} distro={DEFAULT_DISTRO} not in tags, skipping...")
            continue
        canonical_version = canonical_image.replace(f"-{DEFAULT_DISTRO}", "")
        versions.append({"canonical_version": canonical_version, "key": ver})

    return sorted(versions, key=lambda v: by_semver_key(v["canonical_version"]), reverse=True)


def version_combinations(nodejs_versions, python_versions):
    versions = []
    for p in python_versions:
        for n in nodejs_versions:
            distro = f'-{p["distro"]}' if p["distro"] != DEFAULT_DISTRO else ""
            key = f'python{p["key"]}-nodejs{n["key"]}{distro}'
            versions.append(
                {
                    "key": key,
                    "python": p["key"],
                    "python_canonical": p["canonical_version"],
                    "python_image": p["image"],
                    "nodejs": n["key"],
                    "nodejs_canonical": n["canonical_version"],
                    "distro": p["distro"],
                }
            )

    versions = sorted(versions, key=lambda v: DISTROS.index(v["distro"]))
    versions = sorted(versions, key=lambda v: by_semver_key(v["nodejs_canonical"]), reverse=True)
    versions = sorted(versions, key=lambda v: by_semver_key(v["python_canonical"]), reverse=True)
    return versions


def decide_version_combinations(distros):
    distros = list(set(distros))
    # Use the latest patch version from each minor
    python_versions = decide_python_versions(distros)
    # Use the latest minor version from each major
    nodejs_versions = decide_nodejs_versions()
    return version_combinations(nodejs_versions, python_versions)


def persist_versions(versions, dry_run=False):
    if dry_run:
        return
    with VERSIONS_PATH.open("w+") as fp:
        json.dump({"versions": versions}, fp, indent=2)


def load_versions():
    with VERSIONS_PATH.open() as fp:
        return json.load(fp)["versions"]


def find_new_or_updated(current_versions, versions, force=False):
    current_versions = {ver["key"]: ver for ver in current_versions}
    versions = {ver["key"]: ver for ver in versions}
    new_or_updated = []

    for key, ver in versions.items():
        updated = key in current_versions and ver != current_versions[key]
        new = key not in current_versions
        if new or updated or force:
            new_or_updated.append(ver)

    return new_or_updated
