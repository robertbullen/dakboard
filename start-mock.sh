#!/usr/bin/env bash

GPIOZERO_PIN_FACTORY=mock python3 -m interdaktive \
    --control-button-pin=BOARD36 \
    --display-type=mock \
    --export-diagram-file-path='doc/state-machine.png' \
    --motion-sensor-pin=BOARD7 \
    --motion-led-pin=BOARD22 \
    --running-led-pin=BOARD18 \
    --timer-seconds=3 \
    --waking-hours-begin=06:00 \
    --waking-hours-end=22:00
