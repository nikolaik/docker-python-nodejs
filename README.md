# 🐳 Python with Node.js

[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2023-06-22

The `latest` tag is currently:

- Node.js: 20.x
- npm: 9.x
- yarn: stable
- Python: latest
- pip: latest
- pipenv: latest
- poetry: latest

## 🏷 Tags

To use a specific combination of Python and Node.js see the following table of available image tags.

<!-- TAGS_START -->

Tag | Python version | Node.js version | Distro | Platforms
--- | --- | --- | --- | ---
`python3.11-nodejs20` | 3.11.4 | 20.3.1 | buster | linux/amd64, linux/arm64
`python3.11-nodejs20-bullseye` | 3.11.4 | 20.3.1 | bullseye | linux/amd64, linux/arm64
`python3.11-nodejs20-slim` | 3.11.4 | 20.3.1 | slim | linux/amd64, linux/arm64
`python3.11-nodejs20-alpine` | 3.11.4 | 20.3.1 | alpine | linux/amd64
`python3.11-nodejs18` | 3.11.4 | 18.16.1 | buster | linux/amd64, linux/arm64
`python3.11-nodejs18-bullseye` | 3.11.4 | 18.16.1 | bullseye | linux/amd64, linux/arm64
`python3.11-nodejs18-slim` | 3.11.4 | 18.16.1 | slim | linux/amd64, linux/arm64
`python3.11-nodejs18-alpine` | 3.11.4 | 18.16.1 | alpine | linux/amd64
`python3.11-nodejs16` | 3.11.4 | 16.20.1 | buster | linux/amd64, linux/arm64
`python3.11-nodejs16-bullseye` | 3.11.4 | 16.20.1 | bullseye | linux/amd64, linux/arm64
`python3.11-nodejs16-slim` | 3.11.4 | 16.20.1 | slim | linux/amd64, linux/arm64
`python3.11-nodejs16-alpine` | 3.11.4 | 16.20.1 | alpine | linux/amd64
`python3.10-nodejs20` | 3.10.12 | 20.3.1 | buster | linux/amd64, linux/arm64
`python3.10-nodejs20-bullseye` | 3.10.12 | 20.3.1 | bullseye | linux/amd64, linux/arm64
`python3.10-nodejs20-slim` | 3.10.12 | 20.3.1 | slim | linux/amd64, linux/arm64
`python3.10-nodejs20-alpine` | 3.10.12 | 20.3.1 | alpine | linux/amd64
`python3.10-nodejs18` | 3.10.12 | 18.16.1 | buster | linux/amd64, linux/arm64
`python3.10-nodejs18-bullseye` | 3.10.12 | 18.16.1 | bullseye | linux/amd64, linux/arm64
`python3.10-nodejs18-slim` | 3.10.12 | 18.16.1 | slim | linux/amd64, linux/arm64
`python3.10-nodejs18-alpine` | 3.10.12 | 18.16.1 | alpine | linux/amd64
`python3.10-nodejs16` | 3.10.12 | 16.20.1 | buster | linux/amd64, linux/arm64
`python3.10-nodejs16-bullseye` | 3.10.12 | 16.20.1 | bullseye | linux/amd64, linux/arm64
`python3.10-nodejs16-slim` | 3.10.12 | 16.20.1 | slim | linux/amd64, linux/arm64
`python3.10-nodejs16-alpine` | 3.10.12 | 16.20.1 | alpine | linux/amd64
`python3.9-nodejs20` | 3.9.17 | 20.3.1 | buster | linux/amd64, linux/arm64
`python3.9-nodejs20-bullseye` | 3.9.17 | 20.3.1 | bullseye | linux/amd64, linux/arm64
`python3.9-nodejs20-slim` | 3.9.17 | 20.3.1 | slim | linux/amd64, linux/arm64
`python3.9-nodejs20-alpine` | 3.9.17 | 20.3.1 | alpine | linux/amd64
`python3.9-nodejs18` | 3.9.17 | 18.16.1 | buster | linux/amd64, linux/arm64
`python3.9-nodejs18-bullseye` | 3.9.17 | 18.16.1 | bullseye | linux/amd64, linux/arm64
`python3.9-nodejs18-slim` | 3.9.17 | 18.16.1 | slim | linux/amd64, linux/arm64
`python3.9-nodejs18-alpine` | 3.9.17 | 18.16.1 | alpine | linux/amd64
`python3.9-nodejs16` | 3.9.17 | 16.20.1 | buster | linux/amd64, linux/arm64
`python3.9-nodejs16-bullseye` | 3.9.17 | 16.20.1 | bullseye | linux/amd64, linux/arm64
`python3.9-nodejs16-slim` | 3.9.17 | 16.20.1 | slim | linux/amd64, linux/arm64
`python3.9-nodejs16-alpine` | 3.9.17 | 16.20.1 | alpine | linux/amd64
`python3.8-nodejs20` | 3.8.17 | 20.3.1 | buster | linux/amd64, linux/arm64
`python3.8-nodejs20-bullseye` | 3.8.17 | 20.3.1 | bullseye | linux/amd64, linux/arm64
`python3.8-nodejs20-slim` | 3.8.17 | 20.3.1 | slim | linux/amd64, linux/arm64
`python3.8-nodejs20-alpine` | 3.8.17 | 20.3.1 | alpine | linux/amd64
`python3.8-nodejs18` | 3.8.17 | 18.16.1 | buster | linux/amd64, linux/arm64
`python3.8-nodejs18-bullseye` | 3.8.17 | 18.16.1 | bullseye | linux/amd64, linux/arm64
`python3.8-nodejs18-slim` | 3.8.17 | 18.16.1 | slim | linux/amd64, linux/arm64
`python3.8-nodejs18-alpine` | 3.8.17 | 18.16.1 | alpine | linux/amd64
`python3.8-nodejs16` | 3.8.17 | 16.20.1 | buster | linux/amd64, linux/arm64
`python3.8-nodejs16-bullseye` | 3.8.17 | 16.20.1 | bullseye | linux/amd64, linux/arm64
`python3.8-nodejs16-slim` | 3.8.17 | 16.20.1 | slim | linux/amd64, linux/arm64
`python3.8-nodejs16-alpine` | 3.8.17 | 16.20.1 | alpine | linux/amd64
`python3.7-nodejs20` | 3.7.17 | 20.3.1 | buster | linux/amd64, linux/arm64
`python3.7-nodejs20-bullseye` | 3.7.17 | 20.3.1 | bullseye | linux/amd64, linux/arm64
`python3.7-nodejs20-slim` | 3.7.17 | 20.3.1 | slim | linux/amd64, linux/arm64
`python3.7-nodejs20-alpine` | 3.7.17 | 20.3.1 | alpine | linux/amd64
`python3.7-nodejs18` | 3.7.17 | 18.16.1 | buster | linux/amd64, linux/arm64
`python3.7-nodejs18-bullseye` | 3.7.17 | 18.16.1 | bullseye | linux/amd64, linux/arm64
`python3.7-nodejs18-slim` | 3.7.17 | 18.16.1 | slim | linux/amd64, linux/arm64
`python3.7-nodejs18-alpine` | 3.7.17 | 18.16.1 | alpine | linux/amd64
`python3.7-nodejs16` | 3.7.17 | 16.20.1 | buster | linux/amd64, linux/arm64
`python3.7-nodejs16-bullseye` | 3.7.17 | 16.20.1 | bullseye | linux/amd64, linux/arm64
`python3.7-nodejs16-slim` | 3.7.17 | 16.20.1 | slim | linux/amd64, linux/arm64
`python3.7-nodejs16-alpine` | 3.7.17 | 16.20.1 | alpine | linux/amd64

<!-- TAGS_END -->

Lovely! These tags are kept updated automatically when new minor or patch version are released by [`build_versions/main.py`](./build_versions/main.py), which is run twice a day on [CircleCI](https://circleci.com/gh/nikolaik/docker-python-nodejs).

## Supported versions

<!-- SUPPORTED_VERSIONS_START -->

Python version | Start | End
--- | --- | ---
3.11 | 2022-10-24 | 2027-10
3.10 | 2021-10-04 | 2026-10
3.9 | 2020-10-05 | 2025-10
3.8 | 2019-10-14 | 2024-10
3.7 | 2018-06-27 | 2023-06-27

Node.js version | Start | End
--- | --- | ---
v20 | 2023-04-18 | 2026-04-30
v18 | 2022-04-19 | 2025-04-30
v16 | 2021-04-20 | 2023-09-11

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
