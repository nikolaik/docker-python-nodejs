import argparse

from build_versions.docker_build import build_tag_release
from build_versions.dockerfile import render_all_dockerfiles
from build_versions.readme import update_readme_tags_table
from build_versions.settings import DISTROS
from build_versions.versions import decide_version_combinations, find_new_or_updated, load_versions, persist_versions


def main(distros, dry_run, debug, force):
    current_versions = load_versions()
    versions = decide_version_combinations(distros)

    persist_versions(versions, dry_run)
    update_readme_tags_table(versions, dry_run)

    new_or_updated = find_new_or_updated(current_versions, versions, force)
    if not new_or_updated:
        print("No new or updated versions")
        return

    dockerfiles = render_all_dockerfiles(new_or_updated)
    build_tag_release(dockerfiles, dry_run, debug)

    # FIXME(perf): Generate a CircleCI config file with a workflow (parallel) and trigger this workflow via the API.
    # Ref: https://circleci.com/docs/2.0/api-job-trigger/
    # Ref: https://discuss.circleci.com/t/run-builds-on-circleci-using-a-local-config-file/17355?source_topic_id=19287


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
    parser.add_argument("--debug", action="store_true", help="Write generated dockerfiles to disk")
    parser.add_argument("--force", action="store_true", help="Force build all versions (even old)")
    args = vars(parser.parse_args())
    main(**args)
