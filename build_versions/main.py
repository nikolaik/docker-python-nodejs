import argparse
import logging

from build_versions.ci_matrix import generate_matrix
from build_versions.dockerfiles import render_dockerfile_with_context
from build_versions.logger import init_logging
from build_versions.readme import update_readme_tags_table
from build_versions.settings import DISTROS
from build_versions.versions import decide_version_combinations, find_new_or_updated, load_versions, persist_versions

logger = logging.getLogger("dpn")


def main(args):
    if args.dockerfile_with_context:
        render_dockerfile_with_context(args.dockerfile_with_context, args.dry_run)
        return

    current_versions = load_versions()
    versions = decide_version_combinations(args.distros)
    new_or_updated = find_new_or_updated(current_versions, versions, args.force)

    if args.ci_matrix:
        generate_matrix(new_or_updated, args.ci_event)

    if not new_or_updated and not args.ci_matrix:
        logger.info("No new or updated versions")
        return

    if args.release:
        persist_versions(versions, args.dry_run)
        update_readme_tags_table(versions, args.dry_run)


def parse_args():
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

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    init_logging(args.verbose)
    main(args)
