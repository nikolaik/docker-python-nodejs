from typing import TypedDict

import requests


class DockerImageDict(TypedDict):
    architecture: str
    features: str
    variant: str | None
    digest: str
    os: str
    os_features: str
    os_version: str | None
    size: int
    status: str
    last_pulled: str
    last_pushed: str


class DockerTagDict(TypedDict):
    creator: int
    id: int  # noqa: A003
    images: list[DockerImageDict]
    last_updated: str
    last_updater: int
    last_updater_username: str
    name: str
    repository: int
    full_size: int
    v2: bool
    tag_status: str
    tag_last_pulled: str
    tag_last_pushed: str
    media_type: str
    content_type: str
    digest: str


class DockerTagResponse(TypedDict):
    count: int
    next: str | None  # noqa: A003
    previous: str | None
    results: list[DockerTagDict]


def fetch_tags(package: str, page: int = 1) -> list[DockerTagDict]:
    """Fetch available docker tags."""
    result = requests.get(
        f"https://registry.hub.docker.com/v2/namespaces/library/repositories/{package}/tags",
        params={"page": page, "page_size": 100},
        timeout=10.0,
    )
    result.raise_for_status()
    data: DockerTagResponse = result.json()
    if not data["next"]:
        return data["results"]
    return data["results"] + fetch_tags(package, page=page + 1)
