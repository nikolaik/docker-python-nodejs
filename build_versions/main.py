import argparse

from build_versions.ci_config import generate_config
from build_versions.dockerfile import render_dockerfile_by_config
from build_versions.logger import init_logging
from build_versions.readme import update_readme_tags_table
from build_versions.settings import DISTROS
from build_versions.versions import decide_version_combinations, find_new_or_updated, load_versions, persist_versions


def main(distros, dry_run, force, ci_config, dockerfile_config, release):
    if dockerfile_config:
        render_dockerfile_by_config(dockerfile_config, dry_run)
        return

    current_versions = load_versions()
    versions = decide_version_combinations(distros)
    new_or_updated = find_new_or_updated(current_versions, versions, force)

    if ci_config:
        generate_config(new_or_updated)

    if not new_or_updated:
        print("No new or updated versions")
        return

    if release:
        persist_versions(versions, dry_run)
        update_readme_tags_table(versions, dry_run)


if __name__ == "__main__":
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
        "--dry-run", action="store_true", dest="dry_run", help="Skip persisting, README update, and pushing of builds"
    )
    parser.add_argument("--ci-config", action="store_true", help="Generate CI Config")
    parser.add_argument("--release", action="store_true", help="Persist versions and make a release")
    parser.add_argument(
        "--dockerfile-from-config",
        type=argparse.FileType("r"),
        default=None,
        help="Render a dockerfile based on version config",
    )
    parser.add_argument("--force", action="store_true", help="Force build all versions (even old)")
    parser.add_argument("--verbose", action="store_true", help="Enable debug logging")
    args = parser.parse_args()
    init_logging(args.verbose)
    main(args.distros, args.dry_run, args.force, args.ci_config, args.dockerfile_from_config, args.release)
