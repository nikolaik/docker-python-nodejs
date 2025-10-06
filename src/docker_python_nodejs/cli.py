import argparse
import logging
from pathlib import Path
from typing import Literal, cast

from .build_matrix import build_matrix
from .dockerfiles import render_dockerfile_with_context
from .readme import update_dynamic_readme
from .settings import DISTROS
from .versions import (
    decide_version_combinations,
    find_new_or_updated,
    load_build_contexts,
    persist_versions,
    supported_versions,
)

logger = logging.getLogger("dpn")


class CLIArgs(argparse.Namespace):
    dry_run: bool
    distros: list[str]
    verbose: bool
    command: Literal["dockerfile", "build-matrix", "release"]
    force: bool  # build-matrix and release command arg

    context: str  # dockerfile command arg
    event: str  # build-matrix command arg
    builds_dir: Path  # release command arg


def run_dockerfile(args: CLIArgs) -> None:
    render_dockerfile_with_context(args.context, args.dry_run)


def run_build_matrix(args: CLIArgs) -> None:
    suported_python_versions, suported_nodejs_versions = supported_versions()
    versions = decide_version_combinations(args.distros, suported_python_versions, suported_nodejs_versions)
    new_or_updated = find_new_or_updated(versions, args.force)
    build_matrix(new_or_updated, args.event)


def run_release(args: CLIArgs) -> None:
    versions = load_build_contexts(args.builds_dir)
    new_or_updated = find_new_or_updated(versions, args.force)
    suported_python_versions, suported_nodejs_versions = supported_versions()
    if not new_or_updated:
        logger.info("No new or updated versions")
        return

    persist_versions(versions, args.dry_run)
    update_dynamic_readme(versions, suported_python_versions, suported_nodejs_versions, args.dry_run)


def main(args: CLIArgs) -> None:
    if args.dry_run:
        logger.debug("Dry run, outputing only.")

    if args.command == "dockerfile":
        run_dockerfile(args)
    elif args.command == "build-matrix":
        run_build_matrix(args)
    elif args.command == "release":
        run_release(args)


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
    parser.add_argument("--force", action="store_true", help="Force build all versions (even old)")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")

    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # Dockerfile command
    parser_dockerfile = subparsers.add_parser("dockerfile", help="Render a dockerfile based on version config")
    parser_dockerfile.add_argument("--context", default="", help="Dockerfile version config")

    # Build matrix command
    parser_build_matrix = subparsers.add_parser("build-matrix", help="Generate CI build matrix")
    parser_build_matrix.add_argument(
        "--event",
        default="webhook",
        # https://docs.github.com/en/actions/learn-github-actions/contexts#github-context
        help="GitHub Action event name (github.event_name)",
    )

    # Release command
    parser_release = subparsers.add_parser("release", help="Persist versions and make a release")
    parser_release.add_argument(
        "--builds-dir",
        type=Path,
        required=True,
        help="Builds directory with build context JSON files",
    )

    cli_args = cast("CLIArgs", parser.parse_args())
    if cli_args.command == "release":
        if not cli_args.builds_dir.exists():
            parser.error(f"Builds directory {cli_args.builds_dir.as_posix()} does not exist")

        if not cli_args.builds_dir.is_dir():
            parser.error(f"Builds directory {cli_args.builds_dir.as_posix()} is not a directory")

    return cli_args
