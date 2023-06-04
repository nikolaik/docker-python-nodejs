import dataclasses
import json
from pathlib import Path
from unittest import mock

import pytest

from build_versions.dockerfiles import render_dockerfile_with_context
from build_versions.readme import update_dynamic_readme
from build_versions.settings import BASE_PATH, DOCKERFILES_PATH
from build_versions.versions import (
    BuildVersion,
    SupportedVersion,
    scrape_supported_python_versions,
)


@pytest.fixture(name="build_version")
def build_version_fixture() -> BuildVersion:
    return BuildVersion(
        key="python3.11-nodejs20",
        python="3.11",
        python_canonical="3.11.3",
        python_image="3.11.3-buster",
        nodejs="20",
        nodejs_canonical="20.2.0",
        distro="buster",
        platforms=[
            "linux/amd64",
            "linux/arm64",
        ],
    )


def test_scrape_supported_python_versions() -> None:
    versions = scrape_supported_python_versions()
    assert len(versions) > 0
    first_version = versions[0]
    assert first_version.version
    assert first_version.start
    assert first_version.end


def test_render_dockerfile_with_context(build_version: BuildVersion) -> None:
    file_path = DOCKERFILES_PATH / f"{build_version.key}.Dockerfile"
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
    assert (
        f"`{ver.key}` | {ver.python_canonical} | {ver.nodejs_canonical} | {ver.distro} | {', '.join(ver.platforms)}"
        in readme
    )
    assert f"{python_version.version} | {python_version.start} | {python_version.end}" in readme
    assert f"{node_version.version} | {node_version.start} | {node_version.end}" in readme
