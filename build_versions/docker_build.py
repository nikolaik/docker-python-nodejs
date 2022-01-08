import os
from io import BytesIO
from pathlib import Path

import docker
import docker.errors

from build_versions.settings import DOCKER_IMAGE_NAME


def docker_client_authenticated():
    docker_client = docker.from_env()
    dockerhub_username = os.getenv("DOCKERHUB_USERNAME")
    try:
        docker_client.login(dockerhub_username, os.getenv("DOCKERHUB_PASSWORD"))
    except docker.errors.APIError:
        print(f"Could not login to docker hub with username:'{dockerhub_username}'.")
        print("Is env var DOCKERHUB_USERNAME and DOCKERHUB_PASSWORD set correctly?")
        exit(1)

    return docker_client


def build_tag_release(dockerfiles, dry_run=False, debug=False):
    docker_client = docker_client_authenticated()

    # Build, tag and push images
    for version in dockerfiles:
        dockerfile = version["dockerfile"]
        # docker build wants bytes
        with BytesIO(dockerfile.encode()) as fileobj:
            tag = f"{DOCKER_IMAGE_NAME}:{version['key']}"
            nodejs_version = version["nodejs_canonical"]
            python_version = version["python_canonical"]
            print(
                f"Building image {version['key']} python: {python_version} nodejs: {nodejs_version} ...",
                end="",
                flush=True,
            )
            if not dry_run:
                docker_client.images.build_tag_release(fileobj=fileobj, tag=tag, rm=True, pull=True)
            if debug:
                with Path(f"debug-{version['key']}.Dockerfile").open("w") as debug_file:
                    debug_file.write(fileobj.read().decode("utf-8"))
            print(f" pushing...", flush=True)
            if not dry_run:
                docker_client.images.push(DOCKER_IMAGE_NAME, version["key"])
