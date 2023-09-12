from collections.abc import Mapping
from datetime import datetime
from typing import TypedDict

import requests

todays_date = datetime.utcnow().date().isoformat()


def fetch_node_gpg_keys() -> list[str]:
    """Fetch node signing keys used for release archives."""
    url = "https://raw.githubusercontent.com/nodejs/docker-node/master/keys/node.keys"
    res = requests.get(url, timeout=10.0)
    res.raise_for_status()
    return res.text.strip().split("\n")


class NodeRelease(TypedDict):
    version: str
    date: str
    files: list[str]


def fetch_node_releases() -> list[NodeRelease]:
    """Fetch offical node releases"""
    url = "https://nodejs.org/dist/index.json"
    res = requests.get(url, timeout=10.0)
    res.raise_for_status()
    data: list[NodeRelease] = res.json()
    return data


def fetch_node_unofficial_releases() -> list[NodeRelease]:
    url = "https://unofficial-builds.nodejs.org/download/release/index.json"
    res = requests.get(url, timeout=10.0)
    res.raise_for_status()
    data: list[NodeRelease] = res.json()
    return data


class ReleaseScheduleItem(TypedDict):
    start: str
    lts: str
    maintenance: str
    end: str
    codename: str


def fetch_nodejs_release_schedule() -> Mapping[str, ReleaseScheduleItem]:
    """Download list of official releases, skipping unreleased and unsupported versions"""
    res = requests.get("https://raw.githubusercontent.com/nodejs/Release/master/schedule.json", timeout=10.0)
    res.raise_for_status()
    release_schedule: Mapping[str, ReleaseScheduleItem] = res.json()
    return release_schedule
