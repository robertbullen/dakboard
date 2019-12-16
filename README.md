# dakboard

## Raspberry Pi Configuration

1. Install the HDMI-CEC client.

    ```bash
    sudo apt-get install cec-utils
    ```

2. Start the Python script on boot by adding this line to /etc/rc.local.

    ```bash
    sudo python3 /home/pi/dakboard-wake-on-motion.py &
    ```
