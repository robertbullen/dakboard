#!/usr/bin/env bash

git pull || exit $?
pip3 install -r requirements.txt || exit $?
