#!/usr/bin/env bash

OUTPUT_DIR=$(realpath local)
LOG_FILE="${OUTPUT_DIR}/log.txt"
STATE_DIAGRAM_FILE="${OUTPUT_DIR}/state-diagram.png"

mkdir -p "${OUTPUT_DIR}"

if [ "$1" == 'detector' ]; then
    GPIOZERO_PIN_FACTORY=mock python3 -m interdaktive \
        --control-button-pin=BOARD36 \
        --display-type=mock \
        --motion-sensor-pin=BOARD7 \
        --motion-led-pin=BOARD22 \
        --running-led-pin=BOARD18 \
        --timer-seconds=3 \
        --waking-hours-begin=06:00 \
        --waking-hours-end=24:00 \
        --log-file-path="${LOG_FILE}" \
        --state-diagram-file-path="${STATE_DIAGRAM_FILE}"
fi

if [ "$1" == 'webserver' ]; then
    python3 -m interdaktive.webserver \
        --port=5000 \
        --refresh-seconds=3 \
        --log-file-path="${LOG_FILE}" \
        --state-diagram-file-path="${STATE_DIAGRAM_FILE}"
fi
