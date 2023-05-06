import json
import logging
import os
from pathlib import Path

CI_EVENT_SCHEDULED = "scheduled"

logger = logging.getLogger("dpn")


def _github_action_set_output(key: str, value: str):
    """Write
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
    """
    with Path(os.getenv("GITHUB_OUTPUT")).open("a") as fp:
        fp.write(f"{key}={value}")


def generate_matrix(new_or_updated: list, ci_event: str):
    if not new_or_updated and ci_event == CI_EVENT_SCHEDULED:
        logger.info("\n# Scheduled run with no new or updated versions. Doing nothing.")
        return

    matrix = json.dumps({"include": new_or_updated}) if new_or_updated else ""
    _github_action_set_output("MATRIX", matrix)
    logger.info("\n# New or updated versions:")
    logger.info("Nothing" if not new_or_updated else "\n".join(version["key"] for version in new_or_updated))
