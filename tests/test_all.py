import dataclasses
import json
from pathlib import Path
from typing import Any
from unittest import mock

import pytest
import responses

from build_versions.dockerfiles import render_dockerfile_with_context
from build_versions.readme import update_dynamic_readme
from build_versions.settings import BASE_PATH, DOCKERFILES_PATH
from build_versions.versions import (
    BuildVersion,
    SupportedVersion,
    decide_nodejs_versions,
    decide_version_combinations,
    fetch_supported_nodejs_versions,
    scrape_supported_python_versions,
)


@pytest.fixture(name="build_version")
def build_version_fixture() -> BuildVersion:
    return BuildVersion(
        key="python3.11-nodejs20",
        python="3.11",
        python_canonical="3.11.3",
        python_image="3.11.3-bookworm",
        nodejs="20",
        nodejs_canonical="20.2.0",
        distro="bookworm",
        platforms=[
            "linux/amd64",
            "linux/arm64",
        ],
    )


@pytest.mark.enable_socket()
def test_scrape_supported_python_versions() -> None:
    versions = scrape_supported_python_versions()
    assert len(versions) > 0
    first_version = versions[0]
    assert first_version.version
    assert first_version.start
    assert first_version.end


@responses.activate
def test_render_dockerfile_with_context(build_version: BuildVersion) -> None:
    file_path = DOCKERFILES_PATH / f"{build_version.key}.Dockerfile"
    res_keys = responses.Response(
        method="GET",
        url="https://raw.githubusercontent.com/nodejs/docker-node/master/keys/node.keys",
        body="a\nb\nc",
    )
    responses.add(res_keys)

    render_dockerfile_with_context(json.dumps(dataclasses.asdict(build_version)))
    assert file_path.exists()
    with file_path.open() as fp:
        dockerfile = fp.read()

    assert f"# python: {build_version.python_canonical}" in dockerfile
    assert f"# nodejs: {build_version.nodejs_canonical}" in dockerfile


class MockPath:
    content: str = ""

    def __init__(self: "MockPath", content: str) -> None:
        self.content = content

    def write_text(self: "MockPath", text: str) -> None:
        self.content = text

    def read_text(self: "MockPath") -> str:
        return self.content


def test_update_dynamic_readme(build_version: BuildVersion) -> None:
    ver = build_version
    python_version = SupportedVersion(start="2022-10-24", end="2027-10", version="3.11")
    node_version = SupportedVersion(start="2023-04-18", end="2026-04-30", version="v20")
    initial_content = """
## Tags

<!-- TAGS_START -->

<!-- TAGS_END -->

## Supported Versions

<!-- SUPPORTED_VERSIONS_START -->

<!-- SUPPORTED_VERSIONS_END -->
    """
    mock_path = MockPath(initial_content)

    with mock.patch.multiple(
        Path,
        read_text=mock_path.read_text,
        write_text=mock_path.write_text,
    ):
        update_dynamic_readme([ver], [python_version], [node_version])

        file_path = BASE_PATH / "README.md"
        assert file_path.exists()
        readme = file_path.read_text()
    assert f"`{ver.key}` | {ver.python_canonical} | {ver.nodejs_canonical} | {ver.distro}" in readme
    assert f"{python_version.version} | {python_version.start} | {python_version.end}" in readme
    assert f"{node_version.version} | {node_version.start} | {node_version.end}" in readme


@pytest.fixture(name="python_tags")
def python_tags_fixture() -> dict[str, Any]:
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [
            {
                "name": "3.11.4-bookworm",
                "images": [{"os": "linux", "architecture": "amd64"}, {"os": "linux", "architecture": "arm64"}],
            },
            {
                "name": "3.11.4-alpine",
                "images": [{"os": "linux", "architecture": "amd64"}],
            },
        ],
    }


@pytest.fixture(name="node_releases")
def node_releases_fixture() -> list[dict[str, Any]]:
    return [
        {
            "version": "v20.3.0",
            "date": "2023-09-07",
            "files": [
                "linux-arm64",
                "linux-x64",
            ],
        },
    ]


@pytest.fixture(name="node_unofficial_releases")
def node_unofficial_releases_fixture() -> list[dict[str, Any]]:
    return [
        {
            "version": "v20.3.0",
            "date": "2023-09-07",
            "files": [
                "linux-x64-musl",
            ],
        },
    ]


@responses.activate
def test_decide_version_combinations(
    python_tags: dict[str, Any],
    node_releases: list[dict[str, Any]],
    node_unofficial_releases: list[dict[str, Any]],
) -> None:
    res_python = responses.Response(
        method="GET",
        url="https://registry.hub.docker.com/v2/namespaces/library/repositories/python/tags?page=1&page_size=100",
        json=python_tags,
    )
    responses.add(res_python)
    res_nodejs = responses.Response(
        method="GET",
        url="https://nodejs.org/dist/index.json",
        json=node_releases,
    )
    responses.add(res_nodejs)
    res_nodejs_unoffical = responses.Response(
        method="GET",
        url="https://unofficial-builds.nodejs.org/download/release/index.json",
        json=node_unofficial_releases,
    )
    responses.add(res_nodejs_unoffical)
    python_version = SupportedVersion(start="2022-10-24", end="2027-10", version="3.11")
    node_version = SupportedVersion(start="2023-04-18", end="2026-04-30", version="v20")

    versions = decide_version_combinations(["bookworm", "alpine"], [python_version], [node_version])

    assert versions
    assert len(versions) == python_tags["count"]
    assert versions[0].nodejs_canonical == "20.3.0"
    assert versions[0].python_canonical == "3.11.4"
    assert versions[0].distro == "bookworm"
    assert versions[1].nodejs_canonical == "20.3.0"
    assert versions[1].python_canonical == "3.11.4"
    assert versions[1].distro == "alpine"


# FIXME: Use mock response
@pytest.mark.enable_socket()
def test_decide_nodejs_versions() -> None:
    supported_node_versions = fetch_supported_nodejs_versions()
    distros = ["bookworm", "alpine"]
    versions = decide_nodejs_versions(distros, supported_node_versions)

    assert len(supported_node_versions) * len(distros) == len(versions)
