#!/usr/bin/env bash


DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Builds needed contracts from CasperLabs execution-engine to run network tests.
if [[ -z "$DRONE_BUILD_NUMBER" ]]; then
  # not inside CI, so we are not running in docker.
  docker run --rm -it -v $DIR/wasm:/wasm -v /tmp:/tmp \
         casperlabs/buildenv:latest \
         /bin/bash -c "$(cat $DIR/internal_build_script)"
else
  # inside CI, so we are running in docker and need extra volume for docker.sock
  docker run --rm -it -v $DIR/wasm:/wasm -v /tmp:/tmp \
         -v /var/run/docker.sock:/var/run/docker.sock \
         casperlabs/buildenv:latest \
         /bin/bash -c "$(cat $DIR/internal_build_script)"
fi