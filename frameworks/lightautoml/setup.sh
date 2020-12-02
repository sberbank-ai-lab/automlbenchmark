#!/usr/bin/env bash
HERE=$(dirname "$0")
VERSION=${1:-"latest"}

echo "setting up LightAutoML version $VERSION"

. $HERE/../shared/setup.sh

echo $HERE
cd $HERE/lightautoml || { echo "lightautoml dir does not exist"; exit 1; }


PIP install --upgrade keyrings.alt
PIP install poetry

POETRY config virtualenvs.create false
POETRY lock
POETRY install
