#!/usr/bin/env bash

mkdir -p local/
GPIOZERO_PIN_FACTORY=mock python3 -m interdaktive \
    --control-button-pin=BOARD36 \
    --display-type=mock \
    --motion-sensor-pin=BOARD7 \
    --motion-led-pin=BOARD22 \
    --running-led-pin=BOARD18 \
    \
    --timer-seconds=3 \
    --waking-hours-begin=06:00 \
    --waking-hours-end=24:00 \
    \
    --log-file-path=local/log.txt \
    --state-diagram-file-path=local/state-diagram.png
