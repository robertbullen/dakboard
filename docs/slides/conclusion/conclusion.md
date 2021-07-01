<!-- .slide: id="conclusion-conclusion" -->
# Conclusion

===
<!-- .slide: id="conclusion-comparisons" -->
## Comparing DAKboards

<style>
    #conclusion-comparisons table {
        font-size: smaller;
    }
</style>

|                           | Off-the-Shelf             | Custom-Built                                    | Notes                                       |
| ------------------------- | ------------------------- | ----------------------------------------------- | ------------------------------------------- |
| Cost                      | 🟠 \$400                   | 🟢 $261                                          | Prototype + final                           |
| Pi Model                  | 🟠 Pi 3                    | 🟢 Pi 4                                          | Faster CPU; supports 4K displays            |
| OS Disk                   | 🟠 SD Card                 | 🟢 SSD                                           | Faster, more reliable I/O                   |
| Performance & Reliability | 🟠 Fair                    | 🟢 Great                                         | No more corrupting, crashing, or stuttering |
| Screen                    | 🟠 24" / 1920×1080 / 92ppi | 🟢 25" / 2560×1440 / 117ppi                      | Larger, sharper                             |
| Information Density       | 🟠 Lower                   | 🟢 Higher                                        | More readable font; custom design           |
| Design Scalability        | 🟠 Fair                    | 🟢 Near Pixel-Perfect                            | CSS with relative units and positioning     |
| Power Savings Options     | 🟠 Fixed off-hours         | 🟢 Motion-aware with off-Hours, both overridable | On when you care, off when you don't        |
| Diagnostics & Insights    | 🟠 None                    | 🟢 Website                                       | State machine diagram and log               |

===
<!-- .slide: id="conclusion-benefits" -->
# Personal Benefits

|                        | Off-the-Shelf | Custom-Built | Notes                            |
| ---------------------- | ------------- | ------------ | -------------------------------- |
| Wife Acceptance Factor | 🟠 Good        | 🟢 Better     | Unique and exultable             |
| Pride & Satisfaction   | 🟠 Some        | 🟢 More       | Regularly reminded               |
| Learnings              | 🟠 Little      | 🟢 Tons       | See next slide                   |
| Career-Benefitting     | 🟠 None        | 🟢 Some       | Exposure to new tech; presenting |

===
<!-- .slide: class="columns layout" id="conclusion-learnings" style="font-size: smaller" -->
## Learnings

- Column

    - Hardware
        - Raspberry Pi models, capabilities and limitation, pin features, disk options for performance and reliability
        - HDMI-CEC protocol and commands
        - PIR sensors and basic electronics parts
        - Fritzing for documenting/designing circuits
    - Design
        - Font terminology and features
        - Image color analysis and cohesive color palette selection tools
        - CSS variables and calculations
    - Presenting
        - Reveal.js and creating plugins for it
        - Programmatic webcam access
        - GitHub Pages for hosting this presentation

- Column

    - Python
        - Creating packages and managing dependencies
        - GPIO pin programming paradigms
        - Static typing
        - Multiple inheritance via `mixins`
        - Immutable named tuples via `dataclasses`
        - Custom iterable instances
        - Dynamic module loading
        - File watching, REST server, WebSockets, incompatible threading models
        - Finite state machines

===
<!-- .slide: id="conclusion-plans-and-ideas" -->
## Future Plans and Ideas

- Try pulsing instead of blinking LEDs using PWM via hardware pins or software emulation
- Create different screen layouts with different goals and content and loop them
- Experiment with CSS Grid for arranging dashboard tiles (as opposed to absolute positioning)
- Define systemd template unit files for startup/shutdown

===
<!-- .slide: class="columns layout" id="conclusion-links" -->
## Links

- Column

    ![This Presentation](slides/conclusion/presentation-url-qr-code.svg)

    [This Presentation](https://robertbullen.github.io/dakboard)

- Column

    ![GitHub Repo](slides/conclusion/repo-url-qr-code.svg)

    [GitHub Repo](https://github.com/robertbullen/dakboard)
