# Generated %%NOW%%
# python: %%PYTHON_CANONICAL%%
# nodejs: %%NODEJS_CANONICAL%%
FROM python:%%PYTHON_IMAGE%%
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>

# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_%%NODEJS%%.x
# Ref: https://yarnpkg.com/en/docs/install
RUN \
  apt-get update && \
  apt-get install -yqq apt-transport-https
RUN \
  echo "deb https://deb.nodesource.com/node_%%NODEJS%%.x stretch main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs=$(apt-cache show nodejs|grep Version|grep nodesource|cut -c 10-) yarn && \
  apt-mark hold nodejs && \
  pip install -U pip && pip install pipenv && \
  npm i -g npm@^6 && \
  rm -rf /var/lib/apt/lists/*
