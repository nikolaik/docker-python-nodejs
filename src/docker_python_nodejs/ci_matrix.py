import dataclasses
import json
import logging
import os
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
    with Path(GITHUB_OUTPUT).open("a") as fp:
        fp.write(f"{key}={value}")


def generate_matrix(new_or_updated: "list[BuildVersion]", ci_event: str) -> None:
    if not new_or_updated and ci_event == CI_EVENT_SCHEDULED:
        logger.info("\n# Scheduled run with no new or updated versions. Doing nothing.")
        return

    matrix = json.dumps({"include": [dataclasses.asdict(ver) for ver in new_or_updated]}) if new_or_updated else ""
    _github_action_set_output("MATRIX", matrix)
    logger.info("\n# New or updated versions:")
    logger.info("Nothing" if not new_or_updated else "\n".join(version.key for version in new_or_updated))
