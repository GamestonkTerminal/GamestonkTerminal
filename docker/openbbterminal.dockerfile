ARG OPENBBTERMINAL_DOCKER_IMAGE_PREFIX="ghcr.io/openbb-finance"
ARG OPENBBTERMINAL_DOCKER_DEPS_VERSION="1.2.0"
FROM --platform=linux/amd64 ${OPENBBTERMINAL_DOCKER_IMAGE_PREFIX}/openbbterminal-deps:${OPENBBTERMINAL_DOCKER_DEPS_VERSION}

COPY --chown=python:python . .

CMD ["bash", "docker/entry-point.sh"]
