<!-- .slide: id="software-software" -->

# Software

===

<!-- .slide: id="software-controlling-displays" -->

## Controlling the Display

| Display           | Command      | Notes                                                                                                                                                                                                                            |
| ----------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dell U2518D       | `vcgencmd`   | The Dell doesn't respond to CEC commands—it's a monitor and not a home theater component. It does go to sleep about 15–20 seconds after the HDMI signal turns off, and wakes back up in about 5 seconds when the signal returns. |
| Samsung UN32M5300 | `cec-client` | The Samsung stays on for a long while after the HDMI signal is off, presenting a "No Source" message, which is undesirable. But it responds nicely to CEC commands telling the TV to enter standby mode or active mode.          |

===

<!-- .slide: id="software-python-packages" -->

## Noteworthy Python Packages

===

### argparse

===

### gziozero

===

### transitions

===

### typing + mypy
