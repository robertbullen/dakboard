<!-- .slide: id="hardware-hardware" -->
# Hardware

===
<!-- .slide: class="columns layout" id="hardware-prototype" -->
## Prototype

- Column

    ![Prototype Photo](slides/hardware/prototype.jpg)

- Column

    - Experimentation started with hardware that I mostly already owned...

===
<!-- .slide: class="columns layout" -->
### [Samsung 32" Class M5300 Full HD TV](https://www.samsung.com/us/televisions-home-theater/tvs/full-hd-tvs/32--class-m5300-full-hd-tv-un32m5300afxza/)

- Column

    - Recently retired
    - Full HD (1920×1080) resolution
    - \$0

- Column

    ![Samsung 32" Class M5300 Full HD TV](slides/hardware/samsung-un32m5300.jpg)

===
<!-- .slide: class="columns layout" -->
### [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)

- Column

    ![Raspberry Pi 3 Model B](slides/hardware/raspberry-pi-3.jpg)

- Column

    - Received as a prize at a work function years ago
    - Came with a power supply and heat sinks
    - Sufficient to drive the Full HD TV
    - \$0

===
<!-- .slide: class="columns layout" -->
### [Adafruit PIR Sensor](https://www.adafruit.com/product/189)

- Column

    - Senses motion from the IR emitted by our bodies up to 7 meters away within a 120-degree cone
    - Runs on 5V–12V power and the Pi provides 5V
    - Comes with a 1-foot cable/socket
    - Configurable with different triggering signals, timings, and sensitivities
    - There are cheaper alternatives, but their reviews are poor
    - \$11

- Column

    ![Adafruit PIR Sensor](slides/hardware/adafruit-pir.png)

===
<!-- .slide: class="columns layout" -->
### [Smraza Basic Starter Kit with Breadboard](https://www.amazon.com/gp/product/B01HRR7EBG/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)

- Column

    ![Smraza Basic Starter Kit with Breadboard](slides/hardware/smraza-starter-kit.jpg)

- Column

    - Includes the following necessities and more:
        - Breadboard
        - Power supply
        - LEDs
        - Resistors
        - Push buttons
        - Patch wires
    - \$13

===
### Fritzing Wiring Diagram

![Fritzing Diagram](slides/hardware/fritzing-diagram.png) <!-- .element: style="max-height: 900px;" -->

===
### Pinout.xyz Consolidates Raspberry Pi GPIO Info

<iframe class="stretch" data-src="https://pinout.xyz/"></iframe>

===
### Prototype Costs

| Part                                                                                                                                                 | Cost |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---: |
| [Smraza Basic Starter Kit with Breadboard](https://www.amazon.com/gp/product/B01HRR7EBG/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)            | \$13 |
| [Adafruit PIR Sensor](https://www.adafruit.com/product/189)                                                                                          | \$11 |
| [Samsung 32" Class M5300 Full HD TV](https://www.samsung.com/us/televisions-home-theater/tvs/full-hd-tvs/32--class-m5300-full-hd-tv-un32m5300afxza/) |  \$0 |
| [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)                                                               |  \$0 |
|                                                                                                                                                      | \$24 |

===
<!-- .slide: class="columns layout" id="hardware-final-design" -->
## Final Design

- Column

    - The prototype proved out the concept, so it was time to design a permanent solution
    - The following hardware upgrades were used for the final design

- Column

    ![Final Design](slides/hardware/final-design.jpg)

===
<!-- .slide: class="columns layout" -->
### [Dell UltraSharp 25" QHD Monitor (U2518D)](https://www.dell.com/ng/business/p/dell-u2518d-monitor/pd)

- Column

    ![Dell UltraSharp 25" QHD Monitor (U2518D)](slides/hardware/dell-u2518d.jpg)

- Column

    - The 32" TV was too large and too pixelated for the intended location and viewing distance
    - This monitor has a 25" screen, which is about the right size for this installation
    - Employs an IPS panel with good viewing angles, even in portrait mode
    - Projects a QHD resolution (2560×1440) yielding 117ppi for crisper text and sharper images
    - Purchased used from a coworker
    - \$125

===
<!-- .slide: class="columns layout" -->
### [WALI Monitor Stand](https://www.amazon.com/gp/product/B07S1V2VN7/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

- Column

    - A monitor stand was chosen over wall mounting
    - Two other WALI stands were already present in my home office
        - Affordable, functional, and parts are interchangeable
    - \$38

- Column

    ![WALI Monitor Stand](slides/hardware/wali-monitor-stand.jpg)

===
<!-- .slide: class="columns layout" -->
### [Raspberry Pi 4 Model B with 1GB RAM](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)

- Column

    ![Raspberry Pi 4 Model B with 1GB RAM](slides/hardware/raspberry-pi-4.jpg)

- Column

    - Pi 4 is the only model capable of going above Full HD, up to 4K (3840×2160)
    - Available with 1GB, 2GB, 4GB or 8GB of RAM
    - Also purchased a power supply and inexpensive 16GB microSD
    - \$45

    ***

    - Hindsight:
        - Consider purchasing a Pi with more RAM to avoid needing a separate swap drive
        - Don't use inexpensive microSD cards because they're too unreliable to be an OS drive

===
<!-- .slide: class="columns layout" -->
### [Smraza Case for Raspberry Pi 4 B](https://www.amazon.com/gp/product/B07VDCT57F/ref=ppx_yo_dt_b_asin_title_o04_s01?ie=UTF8&psc=1)

- Column

    - Protects and cools the Pi 4, which can run hot
    - \$10

- Column

    ![Smraza Case for Raspberry Pi 4 B](slides/hardware/smraza-case.jpg)

===
<!-- .slide: class="columns layout" -->
### [Samsung 120GB 2.5-inch SSD 840](https://www.samsung.com/uk/support/model/MZ-7TD120BW/)

- Column

    ![Samsung 120GB 2.5-inch SSD 840](slides/hardware/samsung-mz-7td120.jpg)

- Column

    - Boosts performance and reliability
    - Extracted from a retired computer
    - \$0

===
<!-- .slide: class="columns layout" -->
### [SKL Tech USB 3.0/SATA III Hard Drive Adapter Cable](https://www.amazon.com/Drive-Adapter-Cable-Support-Black/dp/B07S9CKV7X)

- Column

    - Necessary to attach the SSD
    - James A Chambers has a thorough [Pi 4 Bootloader guide](https://jamesachambers.com/new-raspberry-pi-4-bootloader-usb-network-boot-guide/) backed by benchmark data and it recommends a similar but different product for max performance and reliability
    - This one is cheaper and still does the job
    - \$8

- Column

    ![SKL Tech USB 3.0/SATA III Hard Drive Adapter Cable](slides/hardware/skl-tech-usb-sata-adapter.jpg)

===
### Final Design Costs

| Part                                                                                                                                                         |  Cost |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----: |
| [Dell UltraSharp 25" QHD Monitor (U2518D)](https://www.dell.com/en-us/work/shop/dell-ultrasharp-25-monitor-u2518d/apd/210-amll/monitors-monitor-accessories) | \$125 |
| [Raspberry Pi 4 Model B with 1GB RAM](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) and accessories                                          |  \$45 |
| [WALI Monitor Stand](https://www.amazon.com/gp/product/B07S1V2VN7/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)                                          |  \$38 |
| [Adafruit PIR Sensor](https://www.adafruit.com/product/189)                                                                                                  |  \$11 |
| [Smraza Case for Rasberry Pi 4 B](https://www.amazon.com/gp/product/B07VDCT57F/ref=ppx_yo_dt_b_asin_title_o04_s01?ie=UTF8&psc=1)                             |  \$10 |
| [SKL Tech USB 3.0/SATA III Hard Drive Adapter Cable](https://www.amazon.com/Drive-Adapter-Cable-Support-Black/dp/B07S9CKV7X)                                 |    $8 |
| [Samsung 120GB 2.5-inch SSD 840](https://www.samsung.com/uk/support/model/MZ-7TD120BW/)                                                                      |   \$0 |
|                                                                                                                                                              | \$237 |
