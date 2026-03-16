import datetime
import re
from typing import TypedDict

import requests

todays_date = datetime.datetime.now(datetime.UTC).date().isoformat()


class NodeRelease(TypedDict):
    version: str
    date: str
    files: list[str]


def fetch_node_releases() -> list[NodeRelease]:
    """Fetch official node releases"""
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


def fetch_latest_nodejs_version() -> str:
    url = "https://nodejs.org/dist/latest/SHASUMS256.txt"
    res = requests.get(url, timeout=10.0)
    res.raise_for_status()
    match = re.search(r"node-(v\d+\.\d+\.\d+)-", res.text)
    if not match:
        msg = "Could not determine latest Node.js version from SHASUMS256.txt"
        raise ValueError(msg)
    return match.group(1)


class ReleaseScheduleItem(TypedDict):
    start: str
    lts: str
    maintenance: str
    end: str
    codename: str


def fetch_nodejs_release_schedule() -> dict[str, ReleaseScheduleItem]:
    """Download list of official releases, skipping unreleased and unsupported versions"""
    res = requests.get("https://raw.githubusercontent.com/nodejs/Release/master/schedule.json", timeout=10.0)
    res.raise_for_status()
    release_schedule: dict[str, ReleaseScheduleItem] = res.json()
    return release_schedule
