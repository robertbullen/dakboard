#!/usr/bin/env bash

# Declare important paths.
OUTPUT_DIR=/var/log/interdaktive
LOG_FILE="${OUTPUT_DIR}/log.txt"
STATE_DIAGRAM_FILE="${OUTPUT_DIR}/state-diagram.png"

# Ensure that the output directory exists.
mkdir -p "${OUTPUT_DIR}"

# Declare a function that logs messages to the log file in the same format as the webserver.
function log_message() {
    echo -e "$(date '+%F %T,000')\tINFO\t$(basename $0)\t$1" >> "${LOG_FILE}"
}

# Declare a function that starts the detector as a child process, assigns the child process ID to a
# variable, and writes a log message.
DETECTOR_PID=0
function start_detector() {
    python3 -m interdaktive \
        --control-button-pin=BOARD36 \
        --display-type=video-core \
        --motion-sensor-pin=BOARD7 \
        --motion-led-pin=BOARD22 \
        --running-led-pin=BOARD18 \
        --timer-seconds=90 \
        --waking-hours-begin=06:00 \
        --waking-hours-end=22:00 \
        --log-file-path="${LOG_FILE}" \
        --state-diagram-file-path="${STATE_DIAGRAM_FILE}" \
        &
    DETECTOR_PID=$!
    log_message "Started detector ($(ps -o pid= -o command= -p ${DETECTOR_PID} | xargs))"
}

# Declare a function that starts the webserver as a child process, assigns the child process ID to
# a variable, and writes a log message.
WEBSERVER_PID=0
function start_webserver() {
    python3 -m interdaktive.webserver \
        --port=5000 \
        --refresh-seconds=3 \
        --log-file-path="${LOG_FILE}" \
        --state-diagram-file-path="${STATE_DIAGRAM_FILE}" \
        &
    WEBSERVER_PID=$!
    log_message "Started webserver ($(ps -o pid= -o command= -p ${WEBSERVER_PID} | xargs))"
}

# Run an infinite watchdog loop.
while true; do
    ps -p "${DETECTOR_PID}" &> /dev/null || start_detector
    ps -p "${WEBSERVER_PID}" &> /dev/null || start_webserver
    sleep 10
done
