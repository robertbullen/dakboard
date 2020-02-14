#!/usr/bin/env bash

if [ "$1" != '--skip-updates' ]; then
    git pull || exit $?

    pip3 install -r requirements.txt || exit $?
fi

sudo python3 -m interdaktive \
    --control-button-pin=BOARD36 \
    --display-type=video-core \
    --motion-sensor-pin=BOARD7 \
    --motion-led-pin=BOARD22 \
    --running-led-pin=BOARD18 \
    --sleep-delay-seconds=150 \
    --waking-time-begin=06:00 \
    --waking-time-end=22:00 &
