FROM python:latest
MAINTAINER Nikolai R Kristiansen <nikolaik@gmail.com>

# Install node prereqs and nodejs 7.x
# Ref: based on https://deb.nodesource.com/setup_7.x
RUN \
  apt-get update && \
  apt-get install -yqq apt-transport-https
RUN \
  echo "deb https://deb.nodesource.com/node_7.x jessie main" > /etc/apt/sources.list.d/nodesource.list && \
  wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
  apt-get update && \
  apt-get install -yqq nodejs && \
  rm -rf /var/lib/apt/lists/*