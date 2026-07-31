from typing import TYPE_CHECKING

from docker_python_nodejs.versions import _latest_patch

if TYPE_CHECKING:
    from docker_python_nodejs.docker_hub import DockerTagDict


def _docker_tag(name: str) -> DockerTagDict:
    return {
        "name": name,
        "images": [
            {
                "architecture": "amd64",
                "features": "",
                "variant": None,
                "digest": "sha256:abc123",
                "os": "linux",
                "os_features": "",
                "os_version": None,
                "size": 123456,
                "status": "active",
                "last_pulled": "2024-01-01T00:00:00Z",
                "last_pushed": "2024-01-01T00:00:00Z",
            },
            {
                "architecture": "arm64",
                "features": "",
                "variant": None,
                "digest": "sha256:abc123",
                "os": "linux",
                "os_features": "",
                "os_version": None,
                "size": 123456,
                "status": "active",
                "last_pulled": "2024-01-01T00:00:00Z",
                "last_pushed": "2024-01-01T00:00:00Z",
            },
        ],
        "creator": 123456,
        "id": 1,
        "last_updated": "2024-01-01T00:00:00Z",
        "last_updater": 123456,
        "last_updater_username": "user",
        "repository": 123456,
        "full_size": 123456,
        "v2": True,
        "tag_status": "active",
        "tag_last_pulled": "2024-01-01T00:00:00Z",
        "tag_last_pushed": "2024-01-01T00:00:00Z",
        "media_type": "application/vnd.docker.distribution.manifest.v2+json",
        "content_type": "application/vnd.docker.distribution.manifest.v2+json",
        "digest": "sha256:abc123",
    }


def test_latest_patch() -> None:
    tags: list[DockerTagDict] = [
        _docker_tag("3.19.2-trixie"),
        _docker_tag("3.19.3-trixie"),
        _docker_tag("3.19.0-trixie"),
    ]
    ver = "3.19"
    distro = "trixie"
    assert _latest_patch(tags, ver, distro) == "3.19.3-trixie"
