workflow "New workflow" {
  on = "push"
  resolves = ["print versions"]
}

action "docker build" {
  uses = "actions/docker/cli@8cdf801b322af5f369e00d85e9cf3a7122f49108"
  args = "docker build -t python-nodejs ."
}

action "print versions" {
  uses = "actions/docker/cli@8cdf801b322af5f369e00d85e9cf3a7122f49108"
  needs = ["docker build"]
  args = "docker run python-nodejs /bin/sh -c \"python -V && pip --version && pipenv --version && node -v && npm -v && yarn --version\""
}
