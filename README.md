# dakboard

This project takes a [DIY DAKboard](https://blog.dakboard.com/diy-wall-display/) and customizes it with two features:

-   A [Python package](interdaktive/) that interfaces with a PIR motion sensor to programmatically turn the display on and off.
-   [Handwritten CSS](css/purply-derply.css) for a two-column portrait layout that looks like this:

    ![Screenshot](docs/dakboard/img/screenshot.jpg)

    _[Background photo](https://unsplash.com/photos/gE1phX0Lbos) by [Hybrid](https://unsplash.com/@artbyhybrid?utm_medium=referral&utm_campaign=photographer-credit&utm_content=creditBadge) on [Unsplash](https://unsplash.com)._

## Presentation

A slide deck about this project is available at <https://robertbullen.github.io/dakboard/>.

## Credits

This project was sponsored in part by my employer, [Constellation](https://constellationmutual.com/), who allocates its IT employees 12 Personal Hack Days per year to pursue technology-related personal interests as part of its growth and development strategy.

## Software

### Raspberry Pi Configuration

1. Follow the steps found at [DIY Wall Display](https://blog.dakboard.com/diy-wall-display/) until the "Turn the monitor on and off automatically (optional)" section. Rather than control the display on a schedule, as that section explains, this project controls it via a motion sensor.

2. Depending on the display being used, install the HDMI-CEC client. Screenly has a great [article on three ways to turn on/off a monitor](https://www.screenly.io/blog/2017/07/02/how-to-automatically-turn-off-and-on-your-monitor-from-your-raspberry-pi/) programmatically from a Raspberry Pi. That article is two and a half years old at the time of this writing and the installation command is slightly different now:

    ```bash
    sudo apt-get install cec-utils
    ```

    With that information in hand, some trial and error lead me to the most effective command for each of the displays that I tested. Your mileage may vary and you may or may not need the CEC client.

    | Display           | Command      | Notes                                                                                                                                                                                                                                                                                                   |
    | ----------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Dell U2518D       | `vcgencmd`   | The Dell doesn't respond to CEC commands, which I suppose makes sense because the monitor wasn't designed to be connected to a chain of home theater components. It does go to sleep about 15–20 seconds after the HDMI signal turns off, and wakes back up in about 5 seconds when the signal returns. |
    | Samsung UN32M5300 | `cec-client` | The Samsung stays on for a long while after the HDMI signal is off, presenting a "No Source" message, which is undesirable. But it responds nicely to CEC commands telling the TV to enter standby mode or active mode.                                                                                 |

3. Add and configure the USB thumb drive to serve as a swap space.

    I never needed to configure additional swap space on the Pi 3 that I used for prototyping. But running the Pi 4 for a matter of hours or days, the system would eventually encounter an out-of-memory scenario that manifested as a Chromium "Aww, Snap!" error. Perhaps I never ran the Pi 3 for long enough to observe the error. Or maybe running the Pi 4 at 1440p (instead of 1080p) is demanding enough to warrant additional memory. In retrospect I wish I would've opted for the 2GB or 4Gb version of the Pi 4 and avoided this issue altogether.

    Raspbian ships with a preconfigured 100MB swap file at `/var/swap`, which by default resides on the SD card. Simply increasing the size of that swap file made the error go away. However, there are a lot of warnings online advising against using the SD card for swapping because it isn't made for a lot of random I/O and can eventually become corrupted, taking the OS with it.

    So in an effort to heed those warnings, I first tried using [ZRAM](https://github.com/novaspirit/rpi_zram). This approach extended the amount of time between "Aww, Snap!" occurrences, but didn't eliminate them. I settled on using a USB thumb drive for swapping, knowing full well that it isn't a terribly fast or robust solution. I'm OK with that, I just need Chromium and the system to not crash!

    1. Format the USB drive: <https://www.pidramble.com/wiki/benchmarks/external-usb-drives#format-a-usb-connected-drive-on-the-raspberry-pi-in-raspbian>.
    2. Mount the USB drive at an exact location upon boot: <https://www.raspberrypi.org/documentation/configuration/external-storage.md>. I specified `/mnt/usb` as the mount point.
    3. Configure the system to swap memory to the USB drive instead of the SD card: <https://nebl.io/neblio-university/enabling-increasing-raspberry-pi-swap/>. In my case, I changed to the following.

        ```bash
        CONF_SWAPFILE=/mnt/usb/swap
        CONF_SWAPFACTOR=1
        ```

        My system devotes 128MB of its 1GB of RAM to the GPU, leaving 872MB of general purpose memory. Note that `dphys-swapfile` limits the swap file to 50% of the disk size, and half of a 2GB thumb drive (after subtracting partitioning and formatting overhead) equates to about 862MB. So the swap file is about 10MB shy of the `CONF_SWAPFACTOR=1` setting. Observations reveal that this is more than sufficient.

4. Clone the repository to your Raspberry Pi.

    ```bash
    # Substitute your forked repository URL if necessary.
    git clone https://github.com/robertbullen/dakboard.git
    ```

5. Start the Python script on boot by adding this line to /etc/rc.local:

    ```bash
    # This assumes the user is the default (pi) and that the repository has
    # been cloned to that user's home directory.
    cd /home/pi/dakboard && ./update.sh && ./start.sh
    ```
