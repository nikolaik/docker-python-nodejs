[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![CircleCI](https://img.shields.io/circleci/project/github/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://circleci.com/gh/nikolaik/docker-python-nodejs)

Last updated by bot: 2021-07-15

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
`python3.9-nodejs16` | 3.9.6 | 16.5.0 | buster
`python3.9-nodejs16-slim` | 3.9.6 | 16.5.0 | slim
`python3.9-nodejs16-alpine` | 3.9.6 | 16.5.0 | alpine
`python3.9-nodejs14` | 3.9.6 | 14.17.3 | buster
`python3.9-nodejs14-slim` | 3.9.6 | 14.17.3 | slim
`python3.9-nodejs14-alpine` | 3.9.6 | 14.17.3 | alpine
`python3.9-nodejs12` | 3.9.6 | 12.22.3 | buster
`python3.9-nodejs12-slim` | 3.9.6 | 12.22.3 | slim
`python3.9-nodejs12-alpine` | 3.9.6 | 12.22.3 | alpine
`python3.8-nodejs16` | 3.8.11 | 16.5.0 | buster
`python3.8-nodejs16-slim` | 3.8.11 | 16.5.0 | slim
`python3.8-nodejs16-alpine` | 3.8.11 | 16.5.0 | alpine
`python3.8-nodejs14` | 3.8.11 | 14.17.3 | buster
`python3.8-nodejs14-slim` | 3.8.11 | 14.17.3 | slim
`python3.8-nodejs14-alpine` | 3.8.11 | 14.17.3 | alpine
`python3.8-nodejs12` | 3.8.11 | 12.22.3 | buster
`python3.8-nodejs12-slim` | 3.8.11 | 12.22.3 | slim
`python3.8-nodejs12-alpine` | 3.8.11 | 12.22.3 | alpine
`python3.7-nodejs16` | 3.7.11 | 16.5.0 | buster
`python3.7-nodejs16-slim` | 3.7.11 | 16.5.0 | slim
`python3.7-nodejs16-stretch` | 3.7.11 | 16.5.0 | stretch
`python3.7-nodejs16-alpine` | 3.7.11 | 16.5.0 | alpine
`python3.7-nodejs14` | 3.7.11 | 14.17.3 | buster
`python3.7-nodejs14-slim` | 3.7.11 | 14.17.3 | slim
`python3.7-nodejs14-stretch` | 3.7.11 | 14.17.3 | stretch
`python3.7-nodejs14-alpine` | 3.7.11 | 14.17.3 | alpine
`python3.7-nodejs12` | 3.7.11 | 12.22.3 | buster
`python3.7-nodejs12-slim` | 3.7.11 | 12.22.3 | slim
`python3.7-nodejs12-stretch` | 3.7.11 | 12.22.3 | stretch
`python3.7-nodejs12-alpine` | 3.7.11 | 12.22.3 | alpine
`python3.6-nodejs16` | 3.6.14 | 16.5.0 | buster
`python3.6-nodejs16-slim` | 3.6.14 | 16.5.0 | slim
`python3.6-nodejs16-stretch` | 3.6.14 | 16.5.0 | stretch
`python3.6-nodejs16-alpine` | 3.6.14 | 16.5.0 | alpine
`python3.6-nodejs14` | 3.6.14 | 14.17.3 | buster
`python3.6-nodejs14-slim` | 3.6.14 | 14.17.3 | slim
`python3.6-nodejs14-stretch` | 3.6.14 | 14.17.3 | stretch
`python3.6-nodejs14-alpine` | 3.6.14 | 14.17.3 | alpine
`python3.6-nodejs12` | 3.6.14 | 12.22.3 | buster
`python3.6-nodejs12-slim` | 3.6.14 | 12.22.3 | slim
`python3.6-nodejs12-stretch` | 3.6.14 | 12.22.3 | stretch
`python3.6-nodejs12-alpine` | 3.6.14 | 12.22.3 | alpine

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
