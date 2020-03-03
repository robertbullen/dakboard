#!/usr/bin/env bash

sudo python3 -m interdaktive \
    --control-button-pin=BOARD36 \
    --display-type=video-core \
    --motion-sensor-pin=BOARD7 \
    --motion-led-pin=BOARD22 \
    --running-led-pin=BOARD18 \
    --timer-seconds=90 \
    --waking-hours-begin=06:00 \
    --waking-hours-end=22:00 \
    --web-server-port=8088 &
