import logging
import re
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from build_versions.versions import LanguageVersion

logger = logging.getLogger("dpn")


def _format_md_table(columns: list[str], rows: list[list[str]]):
    head = f"{' | '.join(columns)}\n{' | '.join(['---'] * len(columns))}"
    body = "\n".join([" | ".join(row) for row in rows])
    return f"{head}\n{body}\n"


def _replace(name: str, replacement: str, document: str):
    start = f"<!-- {name}_START -->\n"
    end = f"\n<!-- {name}_END -->"
    repl = f"{start}\n{replacement}\n{end}"
    return re.sub(f"{start}(.+?){end}", repl, document, flags=re.MULTILINE | re.DOTALL)


def update_dynamic_readme(
    versions,
    python_versions: "list[LanguageVersion]",
    node_versions: "list[LanguageVersion]",
    dry_run=False,
):
    """Read out current README, format fresh README, write back possible changes"""
    readme_path = Path("README.md")
    with readme_path.open() as fp:
        readme = fp.read()

    readme_new = format_readme(versions, python_versions, node_versions, readme)
    if readme == readme_new:
        logger.debug("Regenerated readme matches existing")
        return

    if not dry_run:
        with readme_path.open("w+") as fp:
            fp.write(readme_new)
    else:
        print(readme_new)


def format_readme(
    versions,
    python_versions: "list[LanguageVersion]",
    node_versions: "list[LanguageVersion]",
    readme: str,
):
    """Format fresh README based on passed in version. Replaces the whole table with new versions."""
    tags_table = format_tags(versions)
    readme_fresh = _replace("TAGS", tags_table, readme)

    supported_versions_table = format_supported_versions(python_versions, node_versions)
    return _replace("SUPPORTED_VERSIONS", supported_versions_table, readme_fresh)


def format_tags(versions):
    headings = ["Tag", "Python version", "Node.js version", "Distro", "Platforms"]
    rows = [
        [f"`{v['key']}`", v["python_canonical"], v["nodejs_canonical"], v["distro"], ", ".join(v["platforms"])]
        for v in versions
    ]
    return _format_md_table(headings, rows)


def format_supported_versions(python_versions: "list[LanguageVersion]", node_versions: "list[LanguageVersion]") -> str:
    headings = ["Python version", "Start", "End"]
    rows = [[ver.version, ver.start, ver.end] for ver in sorted(python_versions, key=lambda x: x.start, reverse=True)]
    python_table = _format_md_table(headings, rows)

    headings_node = ["Node.js version", "Start", "End"]
    rows_node = [
        [ver.version, ver.start, ver.end] for ver in sorted(node_versions, key=lambda x: x.start, reverse=True)
    ]
    node_table = _format_md_table(headings_node, rows_node)

    return f"{python_table}\n{node_table}"
