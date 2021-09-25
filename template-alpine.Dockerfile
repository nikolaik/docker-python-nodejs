# Generated %%NOW%%
# python: %%PYTHON_CANONICAL%%
# nodejs: %%NODEJS_CANONICAL%%
FROM python:%%PYTHON_IMAGE%% as builder

RUN apk add curl gcc musl-dev libffi-dev
RUN pip install cffi
RUN find /root/.cache/pip/wheels -name '*.whl' -exec cp {} / +
# FIXME: poetry: Replace workaround for missing cffi musllinux wheel builds when https://foss.heptapod.net/pypy/cffi/-/issues/509 is ready

FROM python:%%PYTHON_IMAGE%%
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>
# Install node prereqs, nodejs and yarn
# Ref: https://raw.githubusercontent.com/nodejs/docker-node/master/Dockerfile-alpine.template
# Ref: https://yarnpkg.com/en/docs/install

RUN apk add curl libstdc++
RUN curl -fsSLO --compressed "https://unofficial-builds.nodejs.org/download/release/v%%NODEJS_CANONICAL%%/node-v%%NODEJS_CANONICAL%%-linux-x64-musl.tar.xz"
RUN curl -fsSLO --compressed "https://unofficial-builds.nodejs.org/download/release/v%%NODEJS_CANONICAL%%/SHASUMS256.txt"
RUN grep " node-v%%NODEJS_CANONICAL%%-linux-x64-musl.tar.xz\$" SHASUMS256.txt | sha256sum -c -
RUN tar -xf "node-v%%NODEJS_CANONICAL%%-linux-x64-musl.tar.xz" && cp -r /node-v16.10.0-linux-x64-musl/* /usr/local

RUN npm i -g npm@^%%NPM_VERSION%% yarn
RUN pip install -U pip && pip install pipenv
# Poetry
# Mimic what install-poetry.py does without the flexibility (platforms, install sources, etc).
# Also install wheels from builder image
COPY --from=builder /*.whl /
ENV VENV=/opt/poetryvenv
RUN python -m venv $VENV && $VENV/bin/pip install /*.whl && rm /*.whl
RUN $VENV/bin/pip install poetry && ln -s $VENV/bin/poetry /usr/local/bin/poetry
