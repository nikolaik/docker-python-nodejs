[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2021-09-29

## 🐳 Python with Node.js 
The `latest` tag is currently:

- Node: 14.x
- npm: 6.x
- yarn: stable
- Python: latest
- pip: latest
- pipenv: latest
- poetry: latest

## 🏷 Tags
To use a specific combination of Python and Node.js see the following table of available image tags.

Tag | Python version | Node.js version | Distro
--- | --- | --- | ---
`python3.9-nodejs16` | 3.9.7 | 16.10.0 | buster
`python3.9-nodejs16-bullseye` | 3.9.7 | 16.10.0 | bullseye
`python3.9-nodejs16-slim` | 3.9.7 | 16.10.0 | slim
`python3.9-nodejs16-alpine` | 3.9.7 | 16.10.0 | alpine
`python3.9-nodejs14` | 3.9.7 | 14.18.0 | buster
`python3.9-nodejs14-bullseye` | 3.9.7 | 14.18.0 | bullseye
`python3.9-nodejs14-slim` | 3.9.7 | 14.18.0 | slim
`python3.9-nodejs14-alpine` | 3.9.7 | 14.18.0 | alpine
`python3.9-nodejs12` | 3.9.7 | 12.22.6 | buster
`python3.9-nodejs12-bullseye` | 3.9.7 | 12.22.6 | bullseye
`python3.9-nodejs12-slim` | 3.9.7 | 12.22.6 | slim
`python3.9-nodejs12-alpine` | 3.9.7 | 12.22.6 | alpine
`python3.8-nodejs16` | 3.8.12 | 16.10.0 | buster
`python3.8-nodejs16-bullseye` | 3.8.12 | 16.10.0 | bullseye
`python3.8-nodejs16-slim` | 3.8.12 | 16.10.0 | slim
`python3.8-nodejs16-alpine` | 3.8.12 | 16.10.0 | alpine
`python3.8-nodejs14` | 3.8.12 | 14.18.0 | buster
`python3.8-nodejs14-bullseye` | 3.8.12 | 14.18.0 | bullseye
`python3.8-nodejs14-slim` | 3.8.12 | 14.18.0 | slim
`python3.8-nodejs14-alpine` | 3.8.12 | 14.18.0 | alpine
`python3.8-nodejs12` | 3.8.12 | 12.22.6 | buster
`python3.8-nodejs12-bullseye` | 3.8.12 | 12.22.6 | bullseye
`python3.8-nodejs12-slim` | 3.8.12 | 12.22.6 | slim
`python3.8-nodejs12-alpine` | 3.8.12 | 12.22.6 | alpine
`python3.7-nodejs16` | 3.7.12 | 16.10.0 | buster
`python3.7-nodejs16-bullseye` | 3.7.12 | 16.10.0 | bullseye
`python3.7-nodejs16-slim` | 3.7.12 | 16.10.0 | slim
`python3.7-nodejs16-alpine` | 3.7.12 | 16.10.0 | alpine
`python3.7-nodejs14` | 3.7.12 | 14.18.0 | buster
`python3.7-nodejs14-bullseye` | 3.7.12 | 14.18.0 | bullseye
`python3.7-nodejs14-slim` | 3.7.12 | 14.18.0 | slim
`python3.7-nodejs14-alpine` | 3.7.12 | 14.18.0 | alpine
`python3.7-nodejs12` | 3.7.12 | 12.22.6 | buster
`python3.7-nodejs12-bullseye` | 3.7.12 | 12.22.6 | bullseye
`python3.7-nodejs12-slim` | 3.7.12 | 12.22.6 | slim
`python3.7-nodejs12-alpine` | 3.7.12 | 12.22.6 | alpine
`python3.6-nodejs16` | 3.6.15 | 16.10.0 | buster
`python3.6-nodejs16-bullseye` | 3.6.15 | 16.10.0 | bullseye
`python3.6-nodejs16-slim` | 3.6.15 | 16.10.0 | slim
`python3.6-nodejs16-alpine` | 3.6.15 | 16.10.0 | alpine
`python3.6-nodejs14` | 3.6.15 | 14.18.0 | buster
`python3.6-nodejs14-bullseye` | 3.6.15 | 14.18.0 | bullseye
`python3.6-nodejs14-slim` | 3.6.15 | 14.18.0 | slim
`python3.6-nodejs14-alpine` | 3.6.15 | 14.18.0 | alpine
`python3.6-nodejs12` | 3.6.15 | 12.22.6 | buster
`python3.6-nodejs12-bullseye` | 3.6.15 | 12.22.6 | bullseye
`python3.6-nodejs12-slim` | 3.6.15 | 12.22.6 | slim
`python3.6-nodejs12-alpine` | 3.6.15 | 12.22.6 | alpine

Lovely! These tags are kept updated automatically when new minor or patch version are released by [`build_versions.py`](./build_versions.py), which is run twice a day on [CircleCI](https://circleci.com/gh/nikolaik/docker-python-nodejs).

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
