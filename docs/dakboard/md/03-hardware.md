# Hardware

===

## Prototype

![Fritzing Diagram](dakboard/img/fritzing-diagram.png) <!-- .element: style="max-height: 720px" -->

===

<!-- .slide: class="layout-image-left" -->

### [Samsung 32" Class M5300 Full HD TV](https://www.samsung.com/us/televisions-home-theater/tvs/full-hd-tvs/32--class-m5300-full-hd-tv-un32m5300afxza/)

![Samsung 32" Class M5300 Full HD TV](dakboard/img/samsung-un32m5300.jpg)

-   After moving homes we no longer had an obvious spot for this TV, so it was available for experimentation
-   Being a TV, it is more effective to suspend and awake it using the HDMI-CEC protocol
-   Only 70ppi
-   \$0

===

<!-- .slide: class="layout-image-left" -->

### [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)

![Raspberry Pi 3 Model B](dakboard/img/raspberry-pi-3.jpg)

-   I received this as a prize at a work function years ago
-   Can drive resolutions up to Full HD (1920×1080)
-   \$0

===

<!-- .slide: class="layout-image-left" -->

### [Adafruit PIR Sensor](https://www.adafruit.com/product/189)

![Adafruit PIR Sensor](dakboard/img/adafruit-pir.png)

-   Passive Infrared sensor detects motion
-   A nicely detailed [guide](https://cdn-learn.adafruit.com/downloads/pdf/pir-passive-infrared-proximity-motion-sensor.pdf) is available
-   \$11 from Amazon because Adafruit was out of stock!
-   There are cheaper alternatives, but product reviews were poor

===

<!-- .slide: class="layout-image-left" -->

### [Smraza Basic Starter Kit with Breadboard](https://www.amazon.com/gp/product/B01HRR7EBG/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)

![Smraza Basic Starter Kit with Breadboard](dakboard/img/smraza-starter-kit.jpg)

-   I needed a breadboard, power supply, LEDs, resistors, push buttons, and patch wires to familiarize myself with the PIR sensor and programming the Pi's GPIO pins. This kit has all that and more.
-   I feel like owning this kit gives me some hacker cred!
-   \$13

===

## Final Design

The prototype hardware would've been sufficient at longer viewing distances, but close up the 32" Full HD (1080×1920) display is too large and pixelated. The following hardware was used for the final design.

===

<!-- .slide: class="layout-image-left" -->

### [Dell UltraSharp 25" QHD Monitor (U2518D)](https://www.dell.com/en-us/work/shop/dell-ultrasharp-25-monitor-u2518d/apd/210-amll/monitors-monitor-accessories)

![Dell UltraSharp 25" QHD Monitor (U2518D)](dakboard/img/dell-u2518d.jpg) <!-- .element class="product-image" -->

-   Has a 25" screen, which is about the right size for this application
-   Employs an IPS panel with good viewing angles, even in portrait mode
-   Projects a QHD resolution (2560×1440) yielding 117ppi for crisper text and sharper images
-   \$125 used from a coworker

===

<!-- .slide: class="layout-image-left" -->

### [Raspberry Pi 4 Model B with 1GB RAM](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)

![Raspberry Pi 4 Model B with 1GB RAM](dakboard/img/raspberry-pi-4.jpg)

-   Pi 4 is the only model capable of going above Full HD (1920×1080)
-   \$45 included a power supply and inexpensive 16GB microSD
-   Hindsight: purchase a 2GB or 4GB model to avoid the next slide

===

<!-- .slide: class="layout-image-left" -->

### 2GB USB Thumb Drive

![USB Thumb Drive](dakboard/img/usb-thumb-drive.jpg)

-   Needed for swap space
-   \$0 (already owned)
-   Hindsight: Avoid this by purchasing a 2GB or 4GB Pi 4

===

## Costs

===

### Prototype Costs

| Part                                                                                                                                                 | Cost |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---: |
| [Samsung 32" Class M5300 Full HD TV](https://www.samsung.com/us/televisions-home-theater/tvs/full-hd-tvs/32--class-m5300-full-hd-tv-un32m5300afxza/) |  \$0 |
| [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)                                                               |  \$0 |
| [Adafruit PIR Sensor](https://www.adafruit.com/product/189)                                                                                          | \$11 |
| [Smraza Basic Starter Kit with Breadboard](https://www.amazon.com/gp/product/B01HRR7EBG/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)            | \$13 |
|                                                                                                                                                      | \$24 |

===

### Final Design Costs

| Part                                                                                                                                                         |  Cost |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----: |
| [Dell UltraSharp 25" QHD Monitor (U2518D)](https://www.dell.com/en-us/work/shop/dell-ultrasharp-25-monitor-u2518d/apd/210-amll/monitors-monitor-accessories) | \$125 |
| [Raspberry Pi 4 Model B with 1GB RAM](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) and accessories                                          |  \$45 |
| [Adafruit PIR Sensor](https://www.adafruit.com/product/189)                                                                                                  |  \$11 |
| 2GB USB Thumb Drive                                                                                                                                          |   \$0 |
|                                                                                                                                                              | \$181 |

<!-- | [Smraza Case for Rasberry Pi 4 B](https://www.amazon.com/gp/product/B07VDCT57F/ref=ppx_yo_dt_b_asin_title_o04_s01?ie=UTF8&psc=1)                     | \$10 | -->

===

### Costs Compared to Offical DAKboard

TODO: Cost comparison
