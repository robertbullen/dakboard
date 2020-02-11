#!/usr/bin/env bash

sudo GPIOZERO_PIN_FACTORY=mock python3 -m interdaktive \
    --control-button-pin=BOARD36 \
    --display-type=mock \
    --motion-sensor-pin=BOARD7 \
    --motion-led-pin=BOARD22 \
    --running-led-pin=BOARD18 \
    --sleep-delay-seconds=5 \
    --waking-time-begin=06:00 \
    --waking-time-end=22:00
