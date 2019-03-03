[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2018-01-01

## Python with Node.js
The `latest` tag is currently:

- Node: 10.x
- npm: 6.x
- yarn: stable
- Python: latest
- pip: latest
- pipenv: latest

## Tags
To use a specific combination of python and node.js see the following table of available image tags.

Tag | Python version | Node.js version
--- | --- | ---
`python3.7-nodejs11` | 3.7.2 | 11.10.1
`python3.7-nodejs10` | 3.7.2 | 10.15.2
`python3.7-nodejs8` | 3.7.2 | 8.15.1
`python3.7-nodejs6` | 3.7.2 | 6.17.0
`python3.6-nodejs11` | 3.6.8 | 11.10.1
`python3.6-nodejs10` | 3.6.8 | 10.15.2
`python3.6-nodejs8` | 3.6.8 | 8.15.1
`python3.6-nodejs6` | 3.6.8 | 6.17.0
`python3.5-nodejs11` | 3.5.6 | 11.10.1
`python3.5-nodejs10` | 3.5.6 | 10.15.2
`python3.5-nodejs8` | 3.5.6 | 8.15.1
`python3.5-nodejs6` | 3.5.6 | 6.17.0
`python3.4-nodejs11` | 3.4.9 | 11.10.1
`python3.4-nodejs10` | 3.4.9 | 10.15.2
`python3.4-nodejs8` | 3.4.9 | 8.15.1
`python3.4-nodejs6` | 3.4.9 | 6.17.0
`python2.7-nodejs11` | 2.7.15 | 11.10.1
`python2.7-nodejs10` | 2.7.15 | 10.15.2
`python2.7-nodejs8` | 2.7.15 | 8.15.1
`python2.7-nodejs6` | 2.7.15 | 6.17.0

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
