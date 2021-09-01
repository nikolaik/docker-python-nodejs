#!/bin/sh
# Mimic what install-poetry.py does without the flexibility (platforms, install sources, etc).
# Also install wheels from builder image (expected to exist at /)
set -eu

VENV=/opt/poetryvenv
python -m venv $VENV

$VENV/bin/pip install /*.whl
$VENV/bin/pip install poetry
ln -s $VENV/bin/poetry /usr/local/bin/poetry