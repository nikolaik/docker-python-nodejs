# Generated %%NOW%%
# python: %%PYTHON_CANONICAL%%
# nodejs: %%NODEJS_CANONICAL%%
FROM python:%%PYTHON_IMAGE%% AS builder

# FIXME: poetry: Replace workaround for missing cffi/cryptography wheel builds for alpine/musl when https://github.com/pyca/cryptography/pull/6236 is ready
# Install node prereqs, nodejs and yarn
# Ref: https://raw.githubusercontent.com/nodejs/docker-node/master/Dockerfile-alpine.template
# Ref: https://yarnpkg.com/en/docs/install

RUN apk add curl gcc musl-dev libffi-dev openssl-dev cargo
RUN curl -fsSLO --compressed "https://unofficial-builds.nodejs.org/download/release/v%%NODEJS_CANONICAL%%/node-v%%NODEJS_CANONICAL%%-linux-x64-musl.tar.xz"
RUN curl -fsSLO --compressed "https://unofficial-builds.nodejs.org/download/release/v%%NODEJS_CANONICAL%%/SHASUMS256.txt"
RUN grep " node-v%%NODEJS_CANONICAL%%-linux-x64-musl.tar.xz\$" SHASUMS256.txt | sha256sum -c -
RUN tar -xf "node-v%%NODEJS_CANONICAL%%-linux-x64-musl.tar.xz"
RUN pip install cryptography
RUN find /root/.cache/pip/wheels -name '*cryptography*.whl' -exec cp {} / +

FROM python:%%PYTHON_IMAGE%%
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>

RUN apk add --no-cache libstdc++ && pip install -U pip && pip install pipenv
COPY --from=builder /node-v%%NODEJS_CANONICAL%%-linux-x64-musl /usr/local
# The mv's is a workaround for https://github.com/npm/arborist/issues/169
RUN mv /usr/local/lib/node_modules /usr/local/lib/node_modules.tmp && \
  mv /usr/local/lib/node_modules.tmp /usr/local/lib/node_modules && \
  npm i -g npm@^%%NPM_VERSION%% yarn

# Poetry
COPY --from=builder /*.whl .
COPY install-poetry.sh .
RUN ./install-poetry.sh
