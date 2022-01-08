import re
from datetime import datetime
from pathlib import Path

import requests


def _fetch_node_gpg_keys():
    url = "https://raw.githubusercontent.com/nodejs/docker-node/master/keys/node.keys"
    return requests.get(url).text.replace("\n", " ")


def render_dockerfile(version, node_gpg_keys):
    dockerfile_template = Path(f'template-{version["distro"]}.Dockerfile').read_text()
    replace_pattern = re.compile("%%(.+?)%%")

    replacements = {
        # NPM: Hold back on v8 for nodejs<15
        "npm_version": "6" if int(version["nodejs"]) < 15 else "8",
        "now": datetime.utcnow().isoformat()[:-7],
        "node_gpg_keys": node_gpg_keys,
        **version,
    }

    def repl(matchobj):
        key = matchobj.group(1).lower()
        return replacements[key]

    return replace_pattern.sub(repl, dockerfile_template)


def render_all_dockerfiles(new_or_updated):
    node_gpg_keys = _fetch_node_gpg_keys()
    return [ver | {"dockerfile": render_dockerfile(ver, node_gpg_keys)} for ver in new_or_updated]
