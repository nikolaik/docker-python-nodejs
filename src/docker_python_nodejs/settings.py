from pathlib import Path

# Paths
BASE_PATH = Path(__file__).parent.parent.parent
VERSIONS_PATH = BASE_PATH / "versions.json"
DOCKERFILES_PATH = BASE_PATH / "dockerfiles"

DEFAULT_PLATFORMS = ["linux/amd64", "linux/arm64"]
DEFAULT_DISTRO = "trixie"
DISTROS = ["trixie", "bookworm", "slim", "alpine"]
