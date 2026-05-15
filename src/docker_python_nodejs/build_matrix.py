import dataclasses
import json
import logging
import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .versions import BuildVersion

CI_EVENT_SCHEDULED = "scheduled"

logger = logging.getLogger("dpn")

GITHUB_OUTPUT = os.getenv("GITHUB_OUTPUT", "")


def _github_action_set_output(key: str, value: str) -> None:
    """Write
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
    """
    if not GITHUB_OUTPUT:
        print("GITHUB_OUTPUT not set", file=sys.stderr)
        sys.exit(1)

    with Path(GITHUB_OUTPUT).open("a") as fp:
        fp.write(f"{key}={value}\n")


def _build_matrix_json(new_or_updated: list[BuildVersion]) -> str:
    return json.dumps({"include": [dataclasses.asdict(ver) for ver in new_or_updated]}) if new_or_updated else ""


def _build_arch_matrix_json(new_or_updated: list[BuildVersion]) -> str:
    if not new_or_updated:
        return ""

    include: list[dict[str, object]] = []
    for version in new_or_updated:
        include.extend(
            (
                dataclasses.asdict(version)
                | {
                    "platform": platform,
                    "arch": platform.split("/")[1],
                    "runner": "ubuntu-24.04-arm" if platform == "linux/arm64" else "ubuntu-latest",
                }
            )
            for platform in version.platforms
        )

    return json.dumps({"include": include})


def build_matrix(new_or_updated: list[BuildVersion], ci_event: str) -> None:
    if not new_or_updated and ci_event == CI_EVENT_SCHEDULED:
        logger.info("\n# Scheduled run with no new or updated versions. Doing nothing.")
        return

    matrix = _build_matrix_json(new_or_updated)
    arch_matrix = _build_arch_matrix_json(new_or_updated)
    _github_action_set_output("matrix", matrix)
    _github_action_set_output("arch_matrix", arch_matrix)
    logger.info("\n# New or updated versions:")
    logger.info("Nothing" if not new_or_updated else "\n".join(version.key for version in new_or_updated))
