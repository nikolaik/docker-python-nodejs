import argparse
import logging
from typing import cast

from .ci_matrix import generate_matrix
from .dockerfiles import render_dockerfile_with_context
from .readme import format_supported_versions, update_dynamic_readme
from .settings import DISTROS
from .versions import (
    decide_version_combinations,
    fetch_supported_nodejs_versions,
    find_new_or_updated,
    load_versions,
    persist_versions,
    scrape_supported_python_versions,
)

logger = logging.getLogger("dpn")


class CLIArgs(argparse.Namespace):
    dry_run: bool
    distros: list[str]
    ci_matrix: bool
    dockerfile_with_context: str
    ci_event: str
    release: bool
    force: bool
    verbose: bool


def main(args: CLIArgs) -> None:
    if args.dry_run:
        logger.debug("Dry run, outputing only.")

    if args.dockerfile_with_context:
        render_dockerfile_with_context(args.dockerfile_with_context, args.dry_run)
        return

    current_versions = load_versions()
    suported_python_versions = scrape_supported_python_versions()
    suported_nodejs_versions = fetch_supported_nodejs_versions()
    supported_versions = format_supported_versions(suported_python_versions, suported_nodejs_versions)
    logger.debug(f"Found the following supported versions:\n{supported_versions}")

    versions = decide_version_combinations(args.distros, suported_python_versions, suported_nodejs_versions)
    new_or_updated = find_new_or_updated(current_versions, versions, args.force)

    if args.ci_matrix:
        generate_matrix(new_or_updated, args.ci_event)

    if not new_or_updated and not args.ci_matrix:
        logger.info("No new or updated versions")
        return

    if args.release:
        persist_versions(versions, args.dry_run)
        update_dynamic_readme(versions, suported_python_versions, suported_nodejs_versions, args.dry_run)


def parse_args() -> CLIArgs:
    parser = argparse.ArgumentParser(usage="🐳 Build Python with Node.js docker images")
    parser.add_argument(
        "-d",
        "--distros",
        dest="distros",
        nargs="*",
        choices=DISTROS,
        help="Specify which distros to build",
        default=DISTROS,
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        dest="dry_run",
        help="Skip persisting, README update, and pushing of builds",
    )
    parser.add_argument("--ci-matrix", action="store_true", help="Generate CI build matrix")
    parser.add_argument(
        "--ci-event",
        default="webhook",
        # https://docs.github.com/en/actions/learn-github-actions/contexts#github-context
        help="GitHub Action event name (github.event_name)",
    )
    parser.add_argument("--release", action="store_true", help="Persist versions and make a release")
    parser.add_argument("--dockerfile-with-context", default="", help="Render a dockerfile based on version config")
    parser.add_argument("--force", action="store_true", help="Force build all versions (even old)")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")

    return cast(CLIArgs, parser.parse_args())
