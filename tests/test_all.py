import dataclasses
import json

from build_versions.dockerfiles import render_dockerfile_with_context
from build_versions.settings import DOCKERFILES_PATH
from build_versions.versions import BuildVersion, scrape_supported_python_versions


def test_scrape_supported_python_versions() -> None:
    versions = scrape_supported_python_versions()
    assert len(versions) > 0
    first_version = versions[0]
    assert first_version.version
    assert first_version.start
    assert first_version.end


def test_render_dockerfile_with_context() -> None:
    build_config = BuildVersion(
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
    file_path = DOCKERFILES_PATH / f"{build_config.key}.Dockerfile"
    render_dockerfile_with_context(json.dumps(dataclasses.asdict(build_config)))
    assert file_path.exists()
    with file_path.open() as fp:
        dockerfile = fp.read()

    assert f"# python: {build_config.python_canonical}" in dockerfile
    assert f"# nodejs: {build_config.nodejs_canonical}" in dockerfile
