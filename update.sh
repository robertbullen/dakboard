#!/usr/bin/env bash

git pull || exit $?
sudo pip3 install -r requirements.txt || exit $?
