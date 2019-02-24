[![Pulls](https://img.shields.io/docker/pulls/nikolaik/python-nodejs.svg?style=flat-square)](https://hub.docker.com/r/nikolaik/python-nodejs/)
[![Release](https://img.shields.io/github/release/nikolaik/docker-python-nodejs.svg?style=flat-square)](https://github.com/nikolaik/docker-python-nodejs/releases)

Last updated by bot: 2018-01-01

## Python (latest) with Node.js 10.x based on [beevelop/nodejs-python](https://github.com/beevelop/docker-nodejs-python)
- Node: 10.x
- npm: 6.x
- yarn: stable
- Python: latest
- pip: latest
- pipenv: latest

----
### Pull from Docker Hub
```
docker pull nikolaik/python-nodejs:latest
```

### Build from GitHub
```
docker build -t nikolaik/python-nodejs github.com/nikolaik/docker-python-nodejs
```

### Run image
```
docker run -it nikolaik/python-nodejs bash
```

### Use as base image
```Dockerfile
FROM nikolaik/python-nodejs:latest
```

## Disclaimer
> This is experimental and might break from time to time. Use at your own risk!
