# dakboard

This project takes a DIY [DAKboard](https://dakboard.com) and customizes it with two features:

-   A [Python script](raspberrypi/dakboard-detect-motion.py) and PIR motion detector to turn the display on and off for power savings.
-   [Handwritten CSS](two-column-portrait.css) for a two-column portrait layout that looks like this:

    ![Screenshot](doc/screenshot.jpg)

    _[Background photo](https://unsplash.com/photos/gE1phX0Lbos) by [Hybrid](https://unsplash.com/@artbyhybrid?utm_medium=referral&utm_campaign=photographer-credit&utm_content=creditBadge) on [Unsplash](https://unsplash.com)._

## Hardware

### Final Design

-   [Adafruit PIR Sensor](https://www.adafruit.com/product/189). I purchased this part from Amazon because Adafruit was out of stock!
-   [Dell UltraSharp 25" QHD Monitor (U2518D)](https://www.dell.com/en-us/work/shop/dell-ultrasharp-25-monitor-u2518d/apd/210-amll/monitors-monitor-accessories). I bought this used from a coworker for \$125.
-   [Raspberry Pi 4 Model B](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/). After I bought the QHD (2560×1440) monitor, I wanted to drive it at its native resolution. The Pi 4 is the only model capable of going above Full HD (1920×1080), so I bought one.

### Prototype

Development was conducted on different hardware that I already had before I invested in the equipment above:

-   [Samsung 32" Class M5300 Full HD TV](https://www.samsung.com/us/televisions-home-theater/tvs/full-hd-tvs/32--class-m5300-full-hd-tv-un32m5300afxza/)
-   [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) (rev 1.2 as obtained by the `cat /proc/cpuinfo` command)

## Raspberry Pi Configuration

1. Follow the steps found at [DIY Wall Display](https://blog.dakboard.com/diy-wall-display/) until the "Turn the monitor on and off automatically (optional)" section. Rather than control the display on a schedule, as that section explains, this project controls it via a motion sensor.

2. Depending on the display being used, install the HDMI-CEC client. Screenly has a great [article on three ways to turn on/off a monitor](https://www.screenly.io/blog/2017/07/02/how-to-automatically-turn-off-and-on-your-monitor-from-your-raspberry-pi/) programmatically from a Raspberry Pi. That article is two and a half years old at the time of this writing and the installation command is slightly different now:

    ```bash
    sudo apt-get install cec-utils
    ```

    With that information in hand, some trial and error lead me to the most effective command for each of the displays that I tested. Your mileage may vary and you may or may not need the CEC client.

    | Display           | Command      | Notes                                                                                                                                                                                                                                                                                                       |
    | ----------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Dell U2518D       | `vcgencmd`   | The Dell doesn't respond to CEC commands, which I suppose makes sense because the monitor wasn't designed to be connected to a chain of home theater components. But it does go to sleep about 15–20 seconds after the HDMI signal turns off, and wakes back up in about 5 seconds when the signal returns. |
    | Samsung UN32M5300 | `cec-client` | The Samsung stays on for a long while after the HDMI signal is off, presenting a "No Source" message, which is undesirable. But it responds nicely to CEC commands telling the TV to enter standby mode or active mode.                                                                                     |

3. Start the Python script on boot by adding this line to /etc/rc.local:

    ```bash
    sudo python3 /home/pi/dakboard-detect-motion.py &
    ```
