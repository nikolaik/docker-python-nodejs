from pathlib import Path

# Paths
BASE_PATH = Path(__file__).parent.parent
VERSIONS_PATH = BASE_PATH / "versions.json"
DOCKERFILES_PATH = BASE_PATH / "dockerfiles"
CONFIG_TEMPLATE_PATH = BASE_PATH / ".circleci/config_template.yml"
CONFIG_GENERATED_PATH = BASE_PATH / ".circleci/config_generated.yml"

DEFAULT_PLATFORMS = ["linux/amd64", "linux/arm64"]
DEFAULT_DISTRO = "bookworm"
DISTROS = ["bookworm", "bullseye", "slim", "alpine"]
