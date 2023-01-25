import json
import logging
from datetime import datetime

import requests
from jinja2 import Environment, FileSystemLoader, select_autoescape

from build_versions.settings import DOCKERFILES_PATH

logger = logging.getLogger("dpn")

env = Environment(loader=FileSystemLoader("./templates"), autoescape=select_autoescape())


def _fetch_node_gpg_keys():
    url = "https://raw.githubusercontent.com/nodejs/docker-node/master/keys/node.keys"
    return requests.get(url, timeout=10.0).text.replace("\n", " ")


def _render_template(template_name, **context):
    template = env.get_template(template_name)
    return template.render(**context)


def render_dockerfile(version, node_gpg_keys):
    distro = "debian" if version["distro"] != "alpine" else version["distro"]

    node_major_version = 15
    context = {
        # NPM: Hold back on v8 for nodejs<15
        "npm_version": "6" if int(version["nodejs"]) < node_major_version else "8",
        "now": datetime.utcnow().isoformat()[:-7],
        "node_gpg_keys": node_gpg_keys,
        **version,
        "distro": "bullseye" if version["distro"] == "slim" else version["distro"],  # slim is an image variant
        "distro_variant": "slim" if version["distro"] == "slim" else "full",
    }

    return _render_template(f"{distro}.Dockerfile", **context)


def render_dockerfile_by_config(config, dry_run=False):
    node_gpg_keys = _fetch_node_gpg_keys()
    with config as fp:
        version = json.load(fp)

    dockerfile = render_dockerfile(version, node_gpg_keys)

    filename = f"{version['key']}.Dockerfile"
    logger.debug(f"Writing {filename}")
    if not dry_run:
        if not DOCKERFILES_PATH.exists():
            DOCKERFILES_PATH.mkdir()
        with (DOCKERFILES_PATH / filename).open("w") as fp:
            fp.write(dockerfile)
