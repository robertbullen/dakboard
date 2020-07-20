<!-- .slide: id="software-software" -->
# Software

===
<!-- .slide: id="software-controlling-displays" -->
## Controlling Displays

<style>
    #software-controlling-displays table {
        font-size: smaller;
    }
    #software-controlling-displays table td {
        vertical-align: middle;
    }
    #software-controlling-displays table td:nth-of-type(2) {
        white-space: nowrap;
    }
    #software-controlling-displays table td:nth-of-type(3) {
        font-size: larger;
        text-align: center;
    }
</style>

| Display           | Command      | Results | Notes                                                                                                                               |
| ----------------- | ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Dell U2518D       | `cec-client` | 👎       | The Dell doesn't respond to CEC commands, which is to be expected because it's a computer monitor and not a home theater component. |
| Dell U2518D       | `vcgencmd`   | 👍       | The Dell goes to sleep 15–20 seconds after the HDMI signal turns off, and wakes back up in about 5 seconds when the signal returns. |
| Samsung UN32M5300 | `cec-client` | 👍       | The Samsung responds nicely to CEC commands telling the TV to enter standby mode or active mode.                                    |
| Samsung UN32M5300 | `vcgencmd`   | 👎       | The Samsung stays on for several minutes after the HDMI signal turns off, presenting a "No Source" message, which is undesirable.   |

===
<!-- .slide: id="software-python-packages" -->
## Python Packages

===
### `argparse` for CLI Arguments

```plaintext
usage: python3 -m interdaktive [-h] --motion-sensor-pin MOTION_SENSOR_PIN
                               [--control-button-pin CONTROL_BUTTON_PIN]
                               [--display-type {cec,mock,video-core}]
                               [--motion-led-pin MOTION_LED_PIN]
                               [--running-led-pin RUNNING_LED_PIN]
                               [--timer-seconds TIMER_SECONDS]
                               [--waking-hours-begin WAKING_HOURS_BEGIN]
                               [--waking-hours-end WAKING_HOURS_END]
                               [--log-file-path LOG_FILE_PATH]
                               [--state-diagram-file-path STATE_DIAGRAM_FILE_PATH]

optional arguments:
  -h, --help            show this help message and exit

hardware arguments:
  GPIO pins must be specified in gpiozero pin numbering format, which is
  described at https://gpiozero.readthedocs.io/en/stable/recipes.html#pin-
  numbering.

  --motion-sensor-pin MOTION_SENSOR_PIN
                        The GPIO pin to which the motion sensor is attached.
                        Detecting motion is this package's raison d'être, and
                        no reasonable default can be assumed, so this is the
                        one and only required argument.
  --control-button-pin CONTROL_BUTTON_PIN
                        The GPIO pin to which an optional control button is
                        attached. Pressing the button will forcibly toggle the
                        display, even outside of waking hours. Holding the
                        button for 5 seconds will shutdown the system.
  --display-type {cec,mock,video-core}
                        The type of display that is connected, which
                        determines how it is put to sleep and awakened. A
                        'video-core' display simply responds to the HDMI
                        signal turning off and on; e.g. a computer monitor. A
                        'cec' display responds to HDMI-CEC commands; e.g. a
                        TV. A 'mock' display is useful for testing and simply
                        outputs its state changes to the console.
  --motion-led-pin MOTION_LED_PIN
                        The GPIO pin to which an optional motion indicator LED
                        is attached.
  --running-led-pin RUNNING_LED_PIN
                        The GPIO pin to which an optional running indicator
                        LED is attached.

timing arguments:
  --timer-seconds TIMER_SECONDS
                        The length of time (in seconds) for the display to
                        stay awake/asleep after detecting motion or the
                        control button is pressed. Also the length of time
                        that the display will remain in its forcibly toggled
                        state after pressing the control button.
  --waking-hours-begin WAKING_HOURS_BEGIN
                        The beginning of the daily period (in 24-hour clock
                        format; e.g. 06:00) when detecting motion will wake
                        the display.
  --waking-hours-end WAKING_HOURS_END
                        The end of the daily period (in 24-hour clock format;
                        e.g. 22:00) when detecting motion will wake the
                        display.

output arguments:
  --log-file-path LOG_FILE_PATH
                        The file path to which logging output will be written.
  --state-diagram-file-path STATE_DIAGRAM_FILE_PATH
                        The file path to which state diagram images will be
                        written.
```
<!-- .element: class="stretch" -->

===
<!-- .slide: class="columns layout" -->
### `gziozero` for Controlling GPIO Pins

- Column

    Typical examples using `RPi.GPIO`:

    <pre><code class="language-python" data-line-numbers data-trim>
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    button_pin = 3
    GPIO.setup(button_pin, GPIO.IN, GPIO.PUD_UP)

    led_pin = 5
    GPIO.setup(led_pin, GPIO.OUT)

    while True:
        # Wait for button to be pressed, then turn on the LED.
        GPIO.wait_for_edge(button_pin, GPIO.FALLING)
        GPIO.output(led_pin, GPIO.HIGH)

        # Wait for button to be released, then turn off the LED.
        GPIO.wait_for_edge(button_pin, GPIO.RISING)
        GPIO.output(led_pin, GPIO.LOW)

        # Some loop termination condition...

    GPIO.cleanup()
    </code></pre>

- Column

    Higher level abstractions with `gpiozero`:

    <pre><code class="language-python" data-line-numbers data-trim>
    from gpiozero import LED, Button
  
    button = Button('BOARD3')
    led = LED('BOARD5')

    button.when_pressed = led.on
    button.when_released = led.off
    </code></pre>

    - Reads more succinctly
    - Provides mocking for unit testing
    - Takes care of threading/non-blocking
    - Takes care of cleanup

===
### `typing` & `mypy` for Static Typing

TODO: Python has static typing capabilities <!-- .element: class="todo" -->

===
### `transitions` for Finite State Machines

<pre class="stretch">
    <code
        class="language-python"
        data-line-numbers="115-150"
        data-src="https://raw.githubusercontent.com/robertbullen/dakboard/a1f90fecc8783b1502ec57c9087b514d9a295f26/interdaktive/state_machine.py"
        data-trim
    >
    </code>
</pre>

===
### `watchdog`, `flask` & `flask-socketio` for a Status Webserver

TODO: Cover the status webserver <!-- .element: class="todo" -->
