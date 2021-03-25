#!/bin/bash

set -eu

DEBUG="${DEBUG:-false}"

env | egrep '^(CATTLE_|ADMIN|HARVESTER_|DEBUG|DEFAULT_|DOCKER_|CLOUD_|KUBE|BUILD_NUMBER|SLACK_).*\=.+' | sort > .env

if [ "false" != "${DEBUG}" ]; then
    cat .env
fi
