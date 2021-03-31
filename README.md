[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2021-03-31

## Python with Node.js
The `latest` tag is currently:

- Node: 14.x
- npm: 6.x
- yarn: stable
- Python: latest
- pip: latest
- pipenv: latest
- poetry: latest

## Tags
To use a specific combination of python and node.js see the following table of available image tags.

Tag | Python version | Node.js version | Distro
--- | --- | --- | ---
`python3.9-nodejs15` | 3.9.2 | 15.12.0 | buster
`python3.9-nodejs15-slim` | 3.9.2 | 15.12.0 | slim
`python3.9-nodejs15-alpine` | 3.9.2 | 15.12.0 | alpine
`python3.9-nodejs14` | 3.9.2 | 14.16.0 | buster
`python3.9-nodejs14-slim` | 3.9.2 | 14.16.0 | slim
`python3.9-nodejs14-alpine` | 3.9.2 | 14.16.0 | alpine
`python3.9-nodejs12` | 3.9.2 | 12.22.0 | buster
`python3.9-nodejs12-slim` | 3.9.2 | 12.22.0 | slim
`python3.9-nodejs12-alpine` | 3.9.2 | 12.22.0 | alpine
`python3.9-nodejs10` | 3.9.2 | 10.24.0 | buster
`python3.9-nodejs10-slim` | 3.9.2 | 10.24.0 | slim
`python3.9-nodejs10-alpine` | 3.9.2 | 10.24.0 | alpine
`python3.8-nodejs15` | 3.8.8 | 15.12.0 | buster
`python3.8-nodejs15-slim` | 3.8.8 | 15.12.0 | slim
`python3.8-nodejs15-alpine` | 3.8.8 | 15.12.0 | alpine
`python3.8-nodejs14` | 3.8.8 | 14.16.0 | buster
`python3.8-nodejs14-slim` | 3.8.8 | 14.16.0 | slim
`python3.8-nodejs14-alpine` | 3.8.8 | 14.16.0 | alpine
`python3.8-nodejs12` | 3.8.8 | 12.22.0 | buster
`python3.8-nodejs12-slim` | 3.8.8 | 12.22.0 | slim
`python3.8-nodejs12-alpine` | 3.8.8 | 12.22.0 | alpine
`python3.8-nodejs10` | 3.8.8 | 10.24.0 | buster
`python3.8-nodejs10-slim` | 3.8.8 | 10.24.0 | slim
`python3.8-nodejs10-alpine` | 3.8.8 | 10.24.0 | alpine
`python3.7-nodejs15` | 3.7.10 | 15.12.0 | buster
`python3.7-nodejs15-slim` | 3.7.10 | 15.12.0 | slim
`python3.7-nodejs15-stretch` | 3.7.10 | 15.12.0 | stretch
`python3.7-nodejs15-alpine` | 3.7.10 | 15.12.0 | alpine
`python3.7-nodejs14` | 3.7.10 | 14.16.0 | buster
`python3.7-nodejs14-slim` | 3.7.10 | 14.16.0 | slim
`python3.7-nodejs14-stretch` | 3.7.10 | 14.16.0 | stretch
`python3.7-nodejs14-alpine` | 3.7.10 | 14.16.0 | alpine
`python3.7-nodejs12` | 3.7.10 | 12.22.0 | buster
`python3.7-nodejs12-slim` | 3.7.10 | 12.22.0 | slim
`python3.7-nodejs12-stretch` | 3.7.10 | 12.22.0 | stretch
`python3.7-nodejs12-alpine` | 3.7.10 | 12.22.0 | alpine
`python3.7-nodejs10` | 3.7.10 | 10.24.0 | buster
`python3.7-nodejs10-slim` | 3.7.10 | 10.24.0 | slim
`python3.7-nodejs10-stretch` | 3.7.10 | 10.24.0 | stretch
`python3.7-nodejs10-alpine` | 3.7.10 | 10.24.0 | alpine
`python3.6-nodejs15` | 3.6.13 | 15.12.0 | buster
`python3.6-nodejs15-slim` | 3.6.13 | 15.12.0 | slim
`python3.6-nodejs15-stretch` | 3.6.13 | 15.12.0 | stretch
`python3.6-nodejs15-alpine` | 3.6.13 | 15.12.0 | alpine
`python3.6-nodejs14` | 3.6.13 | 14.16.0 | buster
`python3.6-nodejs14-slim` | 3.6.13 | 14.16.0 | slim
`python3.6-nodejs14-stretch` | 3.6.13 | 14.16.0 | stretch
`python3.6-nodejs14-alpine` | 3.6.13 | 14.16.0 | alpine
`python3.6-nodejs12` | 3.6.13 | 12.22.0 | buster
`python3.6-nodejs12-slim` | 3.6.13 | 12.22.0 | slim
`python3.6-nodejs12-stretch` | 3.6.13 | 12.22.0 | stretch
`python3.6-nodejs12-alpine` | 3.6.13 | 12.22.0 | alpine
`python3.6-nodejs10` | 3.6.13 | 10.24.0 | buster
`python3.6-nodejs10-slim` | 3.6.13 | 10.24.0 | slim
`python3.6-nodejs10-stretch` | 3.6.13 | 10.24.0 | stretch
`python3.6-nodejs10-alpine` | 3.6.13 | 10.24.0 | alpine

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
