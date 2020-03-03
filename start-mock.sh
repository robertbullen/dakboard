#!/usr/bin/env bash

GPIOZERO_PIN_FACTORY=mock python3 -m interdaktive \
    --control-button-pin=BOARD36 \
    --display-type=mock \
    --motion-sensor-pin=BOARD7 \
    --motion-led-pin=BOARD22 \
    --running-led-pin=BOARD18 \
    --timer-seconds=3 \
    --waking-hours-begin=06:00 \
    --waking-hours-end=24:00 \
    --web-server-port=8888
