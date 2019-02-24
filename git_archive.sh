#!/usr/bin/env bash
set -e

if ! [ -z "$(git status --porcelain)" ]; then
    git config --global user.email "$GH_EMAIL" > /dev/null 2>&1
    git config --global user.name "$GH_NAME" > /dev/null 2>&1

    # Update README.md
    sed -i -E "s/Last updated by bot: .*/Last updated by bot: $(date +%Y-%m-%d)/" README.md

    git add data pdfs README.md
    git commit -m '🗃 Updated Dockerfiles [skip ci]'
    git push --quiet origin master
fi