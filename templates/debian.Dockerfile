# Generated {{ now }}
# python: {{ python_canonical }}
# nodejs: {{ nodejs_canonical }}
FROM python:{{ python_image }}
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>

RUN groupadd --gid 1000 pn && useradd --uid 1000 --gid pn --shell /bin/bash --create-home pn
ENV POETRY_HOME=/usr/local
# Install node prereqs, nodejs and yarn
# Ref: https://deb.nodesource.com/setup_{{ nodejs }}.x
# Ref: https://yarnpkg.com/en/docs/install
RUN \
{% if distro_variant == "slim" %}  apt-get update && apt-get install wget gnupg2 -y && \
{% endif %}  echo "deb https://deb.nodesource.com/node_{{ nodejs }}.x bookworm main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs=$(apt-cache show nodejs|grep Version|grep nodesource|cut -c 10-) yarn && \
  apt-mark hold nodejs && \
  pip install -U pip && pip install pipenv && \
  wget -qO- https://install.python-poetry.org | python - && \
  rm -rf /var/lib/apt/lists/*
