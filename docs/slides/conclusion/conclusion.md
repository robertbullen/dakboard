<!-- .slide: id="conclusion-conclusion" -->
# Conclusion

===
<!-- .slide: class="columns layout" id="conclusion-learnings" style="font-size: smaller" -->
## Learnings

- Column

    - Hardware
        - Raspberry Pi models, capabilities, pin features, and programming models
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
        - Static typing
        - Multiple inheritence via mixins
        - Immutable named tuples via dataclasses
        - Custom iterable instances
        - Dynamic module loading
        - File watching, REST server, WebSockets, incompatible threading models
        - Utilizing finite state machines

===
<!-- .slide: id="conclusion-plans-and-ideas" -->
## Future Plans and Ideas

- Try pulsing instead of blinking LEDs using PWM via hardware pins or software emulation
- Create different screen layouts with different goals and content and loop them
- Experiment with CSS Grid for arranging dashboard tiles (as opposed to absolute positioning)
- Define systemd template unit files for startup/shutdown

===
<!-- .slide: id="conclusion-comparisons" -->
### Comparing DAKboards

<style>
    #conclusion-comparison table {
        font-size: smaller;
    }
</style>

|                                | Off-the-Shelf             | Custom-Built               |
| ------------------------------ | ------------------------- | -------------------------- |
| Cost                           | 🟠 \$400                   | 🟢 $261 (prototype + final) |
| Learnings                      | 🟠 None                    | 🟢 Tons!                    |
| Pi Model                       | 🟠 Pi 3                    | 🟢 Pi 4                     |
| OS Disk                        | 🟠 SD Card                 | 🟢 SSD                      |
| Display                        | 🟠 24" / 1920×1080 / 92ppi | 🟢 25" / 2560×1440 / 117ppi |
| Power Savings Options          | 🟠 Fixed Off-Hours         | 🟢 Motion-Aware             |
| Diagnostics                    | 🟠 None                    | 🟢 Website                  |
| Data Density                   | 🟠 Lower                   | 🟢 Higher                   |
| Design Readability/Scalability | 🟠 Fair                    | 🟢 Near Pixel-Perfect       |
| Wife Acceptance Factor         | 🟠 Good                    | 🟢 Better                   |
| Career-Changing Potential      | 🟠 None                    | 🟢 Some                     |

===
<!-- .slide: class="columns layout" id="conclusion-links" -->
## Links

- Column

    ![This Presentation](slides/conclusion/presentation-url-qr-code.svg)

    [This Presentation](https://robertbullen.github.io/dakboard)

- Column

    ![GitHub Repo](slides/conclusion/repo-url-qr-code.svg)

    [GitHub Repo](https://github.com/robertbullen/dakboard)
