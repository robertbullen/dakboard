#!/usr/bin/env bash

if [ "$1" != '--skip-updates' ]; then
    git pull || exit $?

    pip3 install -r requirements.txt || exit $?
fi

sudo python3 -m interdaktive \
    --control-button-pin=BOARD36 \
    --display-type=video-core \
    --idle-timeout-seconds=150 \
    --motion-sensor-pin=BOARD7 \
    --motion-led-pin=BOARD22 \
    --running-led-pin=BOARD18 \
    --waking-hours-begin=06:00 \
    --waking-hours-end=22:00 &
