from pathlib import Path

# Paths
BASE_PATH = Path(__file__).parent.parent
VERSIONS_PATH = BASE_PATH / "versions.json"
DOCKERFILES_PATH = BASE_PATH / "dockerfiles"
CONFIG_TEMPLATE_PATH = BASE_PATH / ".circleci/config_template.yml"
CONFIG_GENERATED_PATH = BASE_PATH / ".circleci/config_generated.yml"

DEFAULT_DISTRO = "buster"
DISTROS = ["buster", "bullseye", "slim", "alpine"]
