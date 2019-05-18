# Generated %%NOW%%
# python: %%PYTHON_CANONICAL%%
# nodejs: %%NODEJS_CANONICAL%%
FROM python:%%PYTHON_IMAGE%% AS builder

# Install node prereqs, nodejs and yarn
# Ref: https://raw.githubusercontent.com/nodejs/docker-node/master/Dockerfile-alpine.template
# Ref: https://yarnpkg.com/en/docs/install

RUN apk add libstdc++ binutils-gold curl g++ gcc gnupg libgcc linux-headers make python
RUN \
  for server in ipv4.pool.sks-keyservers.net keyserver.pgp.com ha.pool.sks-keyservers.net; do \
  # keys from https://github.com/nodejs/node#release-keys
    gpg --keyserver $server --recv-keys %%NODE_GPG_KEYS%% && break; \
  done
RUN curl -fsSLO --compressed "https://nodejs.org/dist/v%%NODEJS_CANONICAL%%/node-v%%NODEJS_CANONICAL%%.tar.xz"
RUN curl -fsSLO --compressed "https://nodejs.org/dist/v%%NODEJS_CANONICAL%%/SHASUMS256.txt.asc"
RUN gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc
RUN grep " node-v%%NODEJS_CANONICAL%%.tar.xz\$" SHASUMS256.txt | sha256sum -c -
RUN tar -xf "node-v%%NODEJS_CANONICAL%%.tar.xz"
RUN \
  cd "node-v%%NODEJS_CANONICAL%%" && \
  ./configure && \
  make -j$(getconf _NPROCESSORS_ONLN) V= && \
  make install

FROM python:%%PYTHON_IMAGE%%
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>

RUN \
  apk add --no-cache libstdc++ && \
  pip install -U pip && pip install pipenv
COPY --from=builder /usr/local /usr/local
RUN npm i -g npm@^6