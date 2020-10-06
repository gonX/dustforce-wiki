FROM gocd/gocd-agent-alpine-3.12:v20.8.0

ADD Gemfile* /df/

USER root

RUN apk update && \
    apk add --no-cache ruby-bundler ruby-json ruby-bigdecimal ruby-dev g++ gcc make musl-dev zlib zlib-dev && \
    bundle config --global --jobs 8 && \
    cd /df && \
    bundle install --system --no-cache && \
    apk del ruby-dev g++ make musl-dev zlib-dev

ENTRYPOINT ["/docker-entrypoint.sh"]

USER 1000
