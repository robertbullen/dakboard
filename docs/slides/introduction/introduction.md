<!-- .slide: id="introduction-introduction" -->
# Introduction

===
<!-- .slide: id="introduction-inspiration" -->
## Inspiration

<style>
    @import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light+Two&display=swap');

    #introduction-inspiration blockquote {
        font-size: larger;
        font-style: normal;
        padding: 40px;
        width: 50%;
    }

    #introduction-inspiration blockquote .wife {
        color: pink;
        text-align: left;
        font-family: 'Shadows Into Light Two', cursive;
        font-size: 90%;
    }
    #introduction-inspiration blockquote .wife::before {
        content: 'Wife:';
        display: inline-block;
        margin-right: 0.5em;
    }

    #introduction-inspiration blockquote .me {
        color: lightblue;
        font-family: monospace;
        text-align: right;
    }
    #introduction-inspiration blockquote .me::before {
        content: 'Me:';
        display: inline-block;
        margin-right: 0.5em;
    }
</style>

> "My friend has a DAKboard and I think we need one." <!-- .element: class="wife" -->
>
> "A what?" <!-- .element: class="me" -->
>
> "..." <!-- .element: class="wife" -->
>
> "I'll look into it." <!-- .element: class="me" -->

===
<!-- .slide: id="introduction-dakboard" -->
### What Is a DAKboard?

![DAKboard Shopping Site](slides/introduction/dakboard-shop.png) <!-- .element: style="max-height: 900px;" -->

===
<!-- markdownlint-disable no-trailing-punctuation -->
### But What Is DAKboard Really?
<!-- markdownlint-enable no-trailing-punctuation -->

<div class="figures equisized">
    <figure class="fragment">
        <p>
            <img alt="DAKboard Console" src="slides/introduction/dakboard-console.png" />
        </p>
        <figcaption>Web console for configuring your dashboard content</figcaption>
    </figure>
    <figure class="fragment">
        <p>
            <img alt="DAKboard Dashboard" src="slides/introduction/dakboard-dashboard.jpg" />
        </p>
        <figcaption>Service that composes and delivers your dashboard as HTML</figcaption>
    </figure>
    <figure class="fragment">
        <p>
            <img alt="DAKboard Device" src="slides/introduction/dakboard-device.jpg" />
        </p>
        <figcaption>Rendered by a Raspberry Pi running Chromium in kiosk mode</figcaption>
    </figure>
</div>

===
### DAKboard Supports DIY

<iframe class="stretch" data-src="https://blog.dakboard.com/diy-wall-display/"></iframe>

===
<!-- .slide: id="introduction-goals" -->
## DIY Goals

- Functional
- Aesthetic
- Personal/Professional

===
<!-- .slide: class="columns layout" -->
### Functional Goals

- Column

    ![Classroom Monthly Calendar](slides/introduction/classroom-monthly-calendar.jpg)

- Column

    - Display content
        - Date and time
        - Weather forecast
        - Consolidated family calendar
        - Photo roll
        - Countdown to the next important event
        - Local news headlines
    - **Control the display intelligently**
        - **Turn on only while viewing**
        - **Keep off during nighttime hours**
        - **Support push-button overriding of those rules**

===
<!-- .slide: class="columns layout" id="introduction-aesthetic-goals" -->
### Aesthetic Goals

<style>
    #no-sign {
        font-size: 500px;
        margin-top: -525px;
        opacity: 0.9;
        position: relative;
        top: -100px;
    }
</style>

- Column

    - Accommodate all the aforementioned content without feeling busy or cluttered
    - Fit into a home, not a business or commercial setting
    - Incorporate nature into the design motif
    - Achieve a high [wife acceptance factor](https://en.wikipedia.org/wiki/Wife_acceptance_factor)

- Column

    ![Example of Ugly Dashboard](slides/introduction/ugly-dashboard.png)

    🚫<!-- .element: id="no-sign" -->

===
<!-- .slide: class="columns layout" -->
### Personal & Professional Goals

- Column

    ![Mario Power-ups](slides/introduction/power-ups.png)

    <!-- markdownlint-disable heading-start-left no-trailing-punctuation -->
    #### Power Up!
    <!-- markdownlint-enable heading-start-left no-trailing-punctuation -->

- Column

    - Learn about programming electronics with Raspberry Pis
    - Delve deeper into the world of Python
    - Add an interesting project to my personal GitHub account...
    - ...With a nice presentation (you're lookin' at it!)
    - Reinforce my employer's decision to provide Personal Hack Days
    - Inspire others to embrace Personal Hack Days
