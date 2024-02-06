#!/usr/bin/env bash

shScript=`basename "$0"`
pyScript="${shScript/.sh/.py}"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)"

pyScript=$DIR"/"$pyScript

sudo -E PYTHONPATH=${DIR}/../../../../Marvel/python:${DIR}/../../../../Marvel/python/marvel/external_interfaces:${DIR}/../../../../Analysis/python:${DIR}/../../../../Production/General/scripts/options:${DIR}/../../../../Marvel/python/blockfills/options:${DIR}/../../../python:/deploy/current/python:.:${PYTHONPATH} python3 -u ${pyScript} $@

