#!/usr/bin/env bash

git pull || exit $?
./install.sh
