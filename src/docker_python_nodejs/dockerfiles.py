import dataclasses
import datetime
import json
import logging
from collections.abc import Mapping
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .settings import DEFAULT_DISTRO, DOCKERFILES_PATH
from .versions import BuildVersion

logger = logging.getLogger("dpn")

env = Environment(loader=FileSystemLoader("./templates"), autoescape=select_autoescape())


def _render_template(template_name: str, context: Mapping[str, Any]) -> str:
    template = env.get_template(template_name)
    return template.render(context)


def render_dockerfile(version: BuildVersion) -> str:
    distro = "debian" if version.distro != "alpine" else version.distro

    context = dataclasses.asdict(version) | {
        "now": datetime.datetime.now(datetime.UTC).isoformat()[:-7],
        "distro": DEFAULT_DISTRO if version.distro == "slim" else version.distro,  # slim is an image variant
        "distro_variant": "slim" if version.distro == "slim" else "full",
    }

    return _render_template(f"{distro}.Dockerfile", context)


def render_dockerfile_with_context(config_json: str, dry_run: bool = False) -> None:
    version = BuildVersion(**json.loads(config_json))

    dockerfile = render_dockerfile(version)

    filename = f"{version.key}.Dockerfile"
    logger.debug(f"Writing {filename}")
    if not dry_run:
        if not DOCKERFILES_PATH.exists():
            DOCKERFILES_PATH.mkdir()

        dockerfile_path = DOCKERFILES_PATH / filename
        dockerfile_path.write_text(dockerfile)
