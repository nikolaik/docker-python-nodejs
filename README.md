[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2019-10-15

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
`python3.7-nodejs12-stretch` | 3.7.4 | 12.12.0 | stretch
`python3.7-nodejs10-stretch` | 3.7.4 | 10.16.3 | stretch
`python3.7-nodejs8-stretch` | 3.7.4 | 8.16.2 | stretch
`python3.7-nodejs12` | 3.7.4 | 12.12.0 | buster
`python3.7-nodejs10` | 3.7.4 | 10.16.3 | buster
`python3.7-nodejs8` | 3.7.4 | 8.16.2 | buster
`python3.7-nodejs12-alpine` | 3.7.4 | 12.12.0 | alpine
`python3.7-nodejs10-alpine` | 3.7.4 | 10.16.3 | alpine
`python3.7-nodejs8-alpine` | 3.7.4 | 8.16.2 | alpine
`python3.6-nodejs12-stretch` | 3.6.9 | 12.12.0 | stretch
`python3.6-nodejs10-stretch` | 3.6.9 | 10.16.3 | stretch
`python3.6-nodejs8-stretch` | 3.6.9 | 8.16.2 | stretch
`python3.6-nodejs12` | 3.6.9 | 12.12.0 | buster
`python3.6-nodejs10` | 3.6.9 | 10.16.3 | buster
`python3.6-nodejs8` | 3.6.9 | 8.16.2 | buster
`python3.6-nodejs12-alpine` | 3.6.9 | 12.12.0 | alpine
`python3.6-nodejs10-alpine` | 3.6.9 | 10.16.3 | alpine
`python3.6-nodejs8-alpine` | 3.6.9 | 8.16.2 | alpine
`python3.5-nodejs12-stretch` | 3.5.7 | 12.12.0 | stretch
`python3.5-nodejs10-stretch` | 3.5.7 | 10.16.3 | stretch
`python3.5-nodejs8-stretch` | 3.5.7 | 8.16.2 | stretch
`python3.5-nodejs12` | 3.5.7 | 12.12.0 | buster
`python3.5-nodejs10` | 3.5.7 | 10.16.3 | buster
`python3.5-nodejs8` | 3.5.7 | 8.16.2 | buster
`python3.5-nodejs12-alpine` | 3.5.7 | 12.12.0 | alpine
`python3.5-nodejs10-alpine` | 3.5.7 | 10.16.3 | alpine
`python3.5-nodejs8-alpine` | 3.5.7 | 8.16.2 | alpine
`python2.7-nodejs12-stretch` | 2.7.16 | 12.12.0 | stretch
`python2.7-nodejs10-stretch` | 2.7.16 | 10.16.3 | stretch
`python2.7-nodejs8-stretch` | 2.7.16 | 8.16.2 | stretch
`python2.7-nodejs12` | 2.7.16 | 12.12.0 | buster
`python2.7-nodejs10` | 2.7.16 | 10.16.3 | buster
`python2.7-nodejs8` | 2.7.16 | 8.16.2 | buster
`python2.7-nodejs12-alpine` | 2.7.16 | 12.12.0 | alpine
`python2.7-nodejs10-alpine` | 2.7.16 | 10.16.3 | alpine
`python2.7-nodejs8-alpine` | 2.7.16 | 8.16.2 | alpine

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
