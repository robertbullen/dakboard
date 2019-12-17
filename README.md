# dakboard

This project takes a DIY [DAKboard](https://dakboard.com) and customizes it with two features:

-   [Handwritten CSS](two-column-portrait.css) for a two-column portrait layout that aims to display a lot of information along with a custom photo album.
-   A [Python script](raspberrypi/dakboard-detect-motion.py) and PIR motion detector to turn the attached TV on and off for power savings.

This is what the screen looks like:

![Screenshot](doc/screenshot.jpg)

_[Background photo](https://unsplash.com/photos/gE1phX0Lbos) by [Hybrid](https://unsplash.com/@artbyhybrid?utm_medium=referral&utm_campaign=photographer-credit&utm_content=creditBadge) on [Unsplash](https://unsplash.com)._

## Hardware

-   [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/). Rev 1.2 as obtained by the `cat /proc/cpuinfo` command. I received this as a prize at a company meeting. It sat around in my home office for a few years because I didn't know what to do with it, until my wife inspired this project.
-   [Samsung 32" Class M5300 Full HD TV](https://www.samsung.com/us/televisions-home-theater/tvs/full-hd-tvs/32--class-m5300-full-hd-tv-un32m5300afxza/). This TV served as a secondary TV for a few years before we moved to a new house and needed something larger.
-   [Adafruit PIR Sensor](https://www.adafruit.com/product/189). I purchased this part from Amazon because Adafruit was out of stock!

## Raspberry Pi Configuration

1. Follow the steps found at [DIY Wall Display](https://blog.dakboard.com/diy-wall-display/) until the "Turn the monitor on and off automatically (optional)" section. Rather than control the display on a schedule, as that section explains, this project controls it via a motion sensor.

2. Install the HDMI-CEC client. Screenly has a [great article](https://www.screenly.io/blog/2017/07/02/how-to-automatically-turn-off-and-on-your-monitor-from-your-raspberry-pi/) on three different methods for turning on/off a monitor from a Raspberry Pi. Because this particular installation connects a Pi to a TV that displays a "No Source" screen when the Pi turns off its HDMI signal, the third method of using a CEC client to explicitly tell the TV to enter standby mode is required. That article is two and a half years old at the time of this writing and the installation command is slightly different now:

    ```bash
    sudo apt-get install cec-utils
    ```

3. Start the Python script on boot by adding this line to /etc/rc.local:

    ```bash
    sudo python3 /home/pi/dakboard-detect-motion.py &
    ```
