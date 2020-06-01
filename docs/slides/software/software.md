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
| Dell U2518D       | `cec-client` | 👎       | The Dell doesn't respond to CEC commands, which makes sense because it's a computer monitor and not a home theater component.       |
| Dell U2518D       | `vcgencmd`   | 👍       | The Dell goes to sleep 15–20 seconds after the HDMI signal turns off, and wakes back up in about 5 seconds when the signal returns. |
| Samsung UN32M5300 | `cec-client` | 👍       | The Samsung responds nicely to CEC commands telling the TV to enter standby mode or active mode.                                    |
| Samsung UN32M5300 | `vcgencmd`   | 👎       | The Samsung stays on for several minutes after the HDMI signal turns off, presenting a "No Source" message, which is undesirable.   |

===
<!-- .slide: id="software-python-packages" -->
## Python Packages

===
### `argparse` for CLI Arguments

TODO: Show usage output <!-- .element: class="todo" -->

===
### `gziozero` for Controlling GPIO Pins

TODO: Compare and contrast with RPI.GPIO <!-- .element: class="todo" -->

===
### `typing` & `mypy` for Static Typing

TODO: Python has static typing capabilities <!-- .element: class="todo" -->

===
### `transitions` for Finite State Machines

TODO: Explain Finite State Machines <!-- .element: class="todo" -->

===
### `watchdog`, `flask` & `flask-socketio` for a Status Webserver

TODO: Cover the status webserver <!-- .element: class="todo" -->
