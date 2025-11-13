# 🐳 Python with Node.js

[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2025-11-13

The `latest` tag is currently:

- Node.js: 22.x
- npm: 10.x
- yarn: stable
- Python: latest
- pip: latest
- pipenv: latest
- poetry: latest
- uv: latest

## 🏷 Tags

To use a specific combination of Python and Node.js see the following table of available image tags.

<!-- TAGS_START -->

Tag | Python version | Node.js version | Distro
--- | --- | --- | ---
`python3.14-nodejs25-alpine` | 3.14.0 | 25.2.0 | alpine
`python3.14-nodejs24-alpine` | 3.14.0 | 24.11.1 | alpine
`python3.14-nodejs22` | 3.14.0 | 22.21.1 | trixie
`python3.14-nodejs22-bookworm` | 3.14.0 | 22.21.1 | bookworm
`python3.14-nodejs22-slim` | 3.14.0 | 22.21.1 | slim
`python3.14-nodejs22-alpine` | 3.14.0 | 22.21.1 | alpine
`python3.14-nodejs20` | 3.14.0 | 20.19.5 | trixie
`python3.14-nodejs20-bookworm` | 3.14.0 | 20.19.5 | bookworm
`python3.14-nodejs20-slim` | 3.14.0 | 20.19.5 | slim
`python3.14-nodejs20-alpine` | 3.14.0 | 20.19.5 | alpine
`python3.13-nodejs25-alpine` | 3.13.9 | 25.2.0 | alpine
`python3.13-nodejs24-alpine` | 3.13.9 | 24.11.1 | alpine
`python3.13-nodejs22` | 3.13.9 | 22.21.1 | trixie
`python3.13-nodejs22-bookworm` | 3.13.9 | 22.21.1 | bookworm
`python3.13-nodejs22-slim` | 3.13.9 | 22.21.1 | slim
`python3.13-nodejs22-alpine` | 3.13.9 | 22.21.1 | alpine
`python3.13-nodejs20` | 3.13.9 | 20.19.5 | trixie
`python3.13-nodejs20-bookworm` | 3.13.9 | 20.19.5 | bookworm
`python3.13-nodejs20-slim` | 3.13.9 | 20.19.5 | slim
`python3.13-nodejs20-alpine` | 3.13.9 | 20.19.5 | alpine
`python3.12-nodejs25-alpine` | 3.12.12 | 25.2.0 | alpine
`python3.12-nodejs24-alpine` | 3.12.12 | 24.11.1 | alpine
`python3.12-nodejs22` | 3.12.12 | 22.21.1 | trixie
`python3.12-nodejs22-bookworm` | 3.12.12 | 22.21.1 | bookworm
`python3.12-nodejs22-slim` | 3.12.12 | 22.21.1 | slim
`python3.12-nodejs22-alpine` | 3.12.12 | 22.21.1 | alpine
`python3.12-nodejs20` | 3.12.12 | 20.19.5 | trixie
`python3.12-nodejs20-bookworm` | 3.12.12 | 20.19.5 | bookworm
`python3.12-nodejs20-slim` | 3.12.12 | 20.19.5 | slim
`python3.12-nodejs20-alpine` | 3.12.12 | 20.19.5 | alpine
`python3.11-nodejs25-alpine` | 3.11.14 | 25.2.0 | alpine
`python3.11-nodejs24-alpine` | 3.11.14 | 24.11.1 | alpine
`python3.11-nodejs22` | 3.11.14 | 22.21.1 | trixie
`python3.11-nodejs22-bookworm` | 3.11.14 | 22.21.1 | bookworm
`python3.11-nodejs22-slim` | 3.11.14 | 22.21.1 | slim
`python3.11-nodejs22-alpine` | 3.11.14 | 22.21.1 | alpine
`python3.11-nodejs20` | 3.11.14 | 20.19.5 | trixie
`python3.11-nodejs20-bookworm` | 3.11.14 | 20.19.5 | bookworm
`python3.11-nodejs20-slim` | 3.11.14 | 20.19.5 | slim
`python3.11-nodejs20-alpine` | 3.11.14 | 20.19.5 | alpine
`python3.10-nodejs25-alpine` | 3.10.19 | 25.2.0 | alpine
`python3.10-nodejs24-alpine` | 3.10.19 | 24.11.1 | alpine
`python3.10-nodejs22` | 3.10.19 | 22.21.1 | trixie
`python3.10-nodejs22-bookworm` | 3.10.19 | 22.21.1 | bookworm
`python3.10-nodejs22-slim` | 3.10.19 | 22.21.1 | slim
`python3.10-nodejs22-alpine` | 3.10.19 | 22.21.1 | alpine
`python3.10-nodejs20` | 3.10.19 | 20.19.5 | trixie
`python3.10-nodejs20-bookworm` | 3.10.19 | 20.19.5 | bookworm
`python3.10-nodejs20-slim` | 3.10.19 | 20.19.5 | slim
`python3.10-nodejs20-alpine` | 3.10.19 | 20.19.5 | alpine

<!-- TAGS_END -->

Lovely! These tags are kept updated automatically when new minor or patch version are released. The python script in [`src/docker_python_nodejs`](./src/docker_python_nodejs/) handling this is run twice a day on [GitHub actions](https://github.com/nikolaik/docker-python-nodejs/actions).

Image tags are built for linux/amd64 and linux/arm64 platforms, except for alpine which is only linux/amd64. See [issue #70](https://github.com/nikolaik/docker-python-nodejs/issues/70) for details.

## Supported versions

<!-- SUPPORTED_VERSIONS_START -->

Python version | Start | End
--- | --- | ---
3.14 | 2025-10-07 | 2030-10
3.13 | 2024-10-07 | 2029-10
3.12 | 2023-10-02 | 2028-10
3.11 | 2022-10-24 | 2027-10
3.10 | 2021-10-04 | 2026-10

Node.js version | Start | End
--- | --- | ---
v25 | 2025-10-15 | 2026-06-01
v24 | 2025-05-06 | 2028-04-30
v22 | 2024-04-24 | 2027-04-30
v20 | 2023-04-18 | 2026-04-30

<!-- SUPPORTED_VERSIONS_END -->

Versions are kept up to date using official sources. For Python we scrape the _Supported Versions_ table at [devguide.python.org/versions](https://devguide.python.org/versions/#supported-versions) and for Node.js we fetch the release schedule JSON from [github.com/nodejs/Release](https://github.com/nodejs/Release/blob/main/schedule.json).

## Typical tasks

```bash
# Pull from Docker Hub
docker pull nikolaik/python-nodejs:latest
# Build from GitHub
docker build -t nikolaik/python-nodejs github.com/nikolaik/docker-python-nodejs
# Run image
docker run -it nikolaik/python-nodejs bash
```

### Use as base image

```Dockerfile
FROM nikolaik/python-nodejs:latest

USER pn
WORKDIR /home/pn/app
```

All images have a default user `pn` with uid 1000 and gid 1000.

## Disclaimer

> This is experimental and might break from time to time. Use at your own risk!
