from datetime import datetime

import requests

from build_versions.versions import SupportedVersion

todays_date = datetime.utcnow().date().isoformat()


def fetch_node_gpg_keys() -> list[str]:
    """Fetch node signing keys used for release archives."""
    url = "https://raw.githubusercontent.com/nodejs/docker-node/master/keys/node.keys"
    res = requests.get(url, timeout=10.0)
    res.raise_for_status()
    return res.text.strip().split("\n")


def fetch_supported_nodejs_versions() -> list[SupportedVersion]:
    """Download list of official releases, skipping unreleased and unsupported versions"""
    result = requests.get("https://raw.githubusercontent.com/nodejs/Release/master/schedule.json", timeout=10.0)
    release_schedule = result.json()

    versions = []
    for ver, detail in release_schedule.items():
        if detail["start"] <= todays_date <= detail["end"]:
            versions.append(SupportedVersion(version=ver, start=detail["start"], end=detail["end"]))

    return versions
