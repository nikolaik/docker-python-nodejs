[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2020-04-14

## Python with Node.js
The `latest` tag is currently:

- Node: 12.x
- npm: 6.x
- yarn: stable
- Python: latest
- pip: latest
- pipenv: latest

## Tags
To use a specific combination of python and node.js see the following table of available image tags.

Tag | Python version | Node.js version | Distro
--- | --- | --- | ---
`python3.8-nodejs13` | 3.8.2 | 13.12.0 | buster
`python3.8-nodejs13-alpine` | 3.8.2 | 13.12.0 | alpine
`python3.8-nodejs12` | 3.8.2 | 12.16.2 | buster
`python3.8-nodejs12-alpine` | 3.8.2 | 12.16.2 | alpine
`python3.8-nodejs10` | 3.8.2 | 10.20.1 | buster
`python3.8-nodejs10-alpine` | 3.8.2 | 10.20.1 | alpine
`python3.7-nodejs13` | 3.7.7 | 13.12.0 | buster
`python3.7-nodejs13-stretch` | 3.7.7 | 13.12.0 | stretch
`python3.7-nodejs13-alpine` | 3.7.7 | 13.12.0 | alpine
`python3.7-nodejs12` | 3.7.7 | 12.16.2 | buster
`python3.7-nodejs12-stretch` | 3.7.7 | 12.16.2 | stretch
`python3.7-nodejs12-alpine` | 3.7.7 | 12.16.2 | alpine
`python3.7-nodejs10` | 3.7.7 | 10.20.1 | buster
`python3.7-nodejs10-stretch` | 3.7.7 | 10.20.1 | stretch
`python3.7-nodejs10-alpine` | 3.7.7 | 10.20.1 | alpine
`python3.6-nodejs13` | 3.6.10 | 13.12.0 | buster
`python3.6-nodejs13-stretch` | 3.6.10 | 13.12.0 | stretch
`python3.6-nodejs13-alpine` | 3.6.10 | 13.12.0 | alpine
`python3.6-nodejs12` | 3.6.10 | 12.16.2 | buster
`python3.6-nodejs12-stretch` | 3.6.10 | 12.16.2 | stretch
`python3.6-nodejs12-alpine` | 3.6.10 | 12.16.2 | alpine
`python3.6-nodejs10` | 3.6.10 | 10.20.1 | buster
`python3.6-nodejs10-stretch` | 3.6.10 | 10.20.1 | stretch
`python3.6-nodejs10-alpine` | 3.6.10 | 10.20.1 | alpine
`python3.5-nodejs13` | 3.5.9 | 13.12.0 | buster
`python3.5-nodejs13-stretch` | 3.5.9 | 13.12.0 | stretch
`python3.5-nodejs13-alpine` | 3.5.9 | 13.12.0 | alpine
`python3.5-nodejs12` | 3.5.9 | 12.16.2 | buster
`python3.5-nodejs12-stretch` | 3.5.9 | 12.16.2 | stretch
`python3.5-nodejs12-alpine` | 3.5.9 | 12.16.2 | alpine
`python3.5-nodejs10` | 3.5.9 | 10.20.1 | buster
`python3.5-nodejs10-stretch` | 3.5.9 | 10.20.1 | stretch
`python3.5-nodejs10-alpine` | 3.5.9 | 10.20.1 | alpine

Lovely! These tags are kept updated automatically (when new minor or patch version are released) by `build_versions.py` which is run twice a day on [CircleCI](https://circleci.com/gh/nikolaik/docker-python-nodejs).

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
```

## Disclaimer
> This is experimental and might break from time to time. Use at your own risk!
