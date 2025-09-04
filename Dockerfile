FROM python:trixie
LABEL org.opencontainers.image.authors="Nikolai R Kristiansen <nikolaik@gmail.com>"

RUN groupadd --gid 1000 pn && useradd --uid 1000 --gid pn --shell /bin/bash --create-home pn
ENV POETRY_HOME=/usr/local

# Install nodejs and yarn
RUN NODE_VERSION="$(curl -fsSL https://nodejs.org/dist/latest/SHASUMS256.txt | head -n1 | awk '{ print $2}' | awk -F - '{ print $2}')" \
  ARCH= && dpkgArch="$(dpkg --print-architecture)" \
  && case "${dpkgArch##*-}" in \
    amd64) ARCH='x64';; \
    arm64) ARCH='arm64';; \
    *) echo "unsupported architecture"; exit 1 ;; \
  esac \
  && for key in $(curl -sL https://raw.githubusercontent.com/nodejs/docker-node/HEAD/keys/node.keys); do \
      gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys "$key" || \
      gpg --batch --keyserver keyserver.ubuntu.com --recv-keys "$key" ; \
  done \
  && curl -fsSLO --compressed "https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-$ARCH.tar.xz" \
  && curl -fsSLO --compressed "https://nodejs.org/dist/$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local --strip-components=1 --no-same-owner \
  && rm "node-$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs
RUN corepack enable yarn
RUN \
  apt-get update && \
  apt-get upgrade -yqq && \
  pip install -U pip pipenv uv && \
  curl -sSL https://install.python-poetry.org | python - && \
  rm -rf /var/lib/apt/lists/*
