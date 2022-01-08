import re
from pathlib import Path


def update_readme_tags_table(versions, dry_run=False):
    readme_path = Path("README.md")
    with readme_path.open() as fp:
        readme = fp.read()

    headings = ["Tag", "Python version", "Node.js version", "Distro"]
    rows = []
    for v in versions:
        rows.append([f"`{v['key']}`", v["python_canonical"], v["nodejs_canonical"], v["distro"]])

    head = f"{' | '.join(headings)}\n{' | '.join(['---' for h in headings])}"
    body = "\n".join([" | ".join(row) for row in rows])
    table = f"{head}\n{body}\n"

    start = "the following table of available image tags.\n"
    end = "\nLovely!"
    sub_pattern = re.compile(f"{start}(.+?){end}", re.MULTILINE | re.DOTALL)

    readme_new = sub_pattern.sub(f"{start}\n{table}{end}", readme)
    if readme != readme_new and not dry_run:
        with readme_path.open("w+") as fp:
            fp.write(readme_new)
