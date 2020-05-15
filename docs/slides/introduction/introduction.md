<!-- .slide: id="introduction-introduction" -->
# Introduction

===
<!-- .slide: id="introduction-inspiration" -->
## Inspiration

<style>
    @import url('https://fonts.googleapis.com/css?family=Indie+Flower&display=swap');

    #introduction-inspiration blockquote {
        font-size: larger;
        font-style: normal;
        padding: 40px;
        width: 50%;
    }

    #introduction-inspiration blockquote .wife {
        color: pink;
        text-align: left;
        font-family: 'Indie Flower', cursive;
        font-size: 110%;
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
<!-- markdownlint-disable no-trailing-punctuation -->
### What Is DAKboard?
<!-- markdownlint-enable no-trailing-punctuation -->

<div class="figures equisized">
    <figure class="fragment">
        <p>
            <img alt="DAKboard Device" src="slides/introduction/dakboard-device.jpg" />
        </p>
        <figcaption>Raspberry Pi running Chrome in full-screen kiosk mode</figcaption>
    </figure>
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
</div>

===
### DAKboard Supports DIY

<iframe class="stretch" data-src="https://blog.dakboard.com/diy-wall-display/"></iframe>

===
<!-- .slide: id="introduction-goals" -->
## Goals

- Functional
- Aesthetic
- Personal/Professional

===
<!-- .slide: class="columns layout" -->
### Functional Goals

- Column

    ![Classroom Monthly Calendar](slides/introduction/classroom-monthly-calendar.jpg)

- Column

    - Display the date, time, and weather
    - Provide a consolidated family calendar
        - Become the successor to the kids' classroom monthly calendar
    - Publish *keeper* photos that are otherwise rarely viewed after capture
    - Control the display intelligently
        - Turn on only while viewing
        - Keep off during nighttime hours

===
<!-- .slide: class="columns layout" id="introduction-aesthetic-goals" -->
### Aesthetic Goals

<style>
 #no-sign {
    font-size: 500px;
    margin-top: -525px;
    position: relative;
    top: -100px;
}
</style>

- Column

    - Design for high data density without feeling busy or cluttered
    - Fit into home decor
    - Incorporate nature into the design motif
    - Achieve a high [wife acceptance factor](https://en.wikipedia.org/wiki/Wife_acceptance_factor)

- Column

    ![Example of Ugly Dashboard](slides/introduction/ugly-dashboard.png)

    🚫<!-- .element: class="fragment fade-in" id="no-sign" -->

===
<!-- .slide: class="columns layout" -->
### Personal/Professional Goals

- Column

    ![Mario Power-ups](slides/introduction/power-ups.png)

    <!-- markdownlint-disable heading-start-left no-trailing-punctuation -->
    #### Power Up!
    <!-- markdownlint-enable heading-start-left no-trailing-punctuation -->

- Column

    - Learn about programming electronics with Raspberry Pis
    - Delve into the world of Python
    - Add an interesting project to my personal GitHub account
    - Excite and inspire others at Constellation to embrace Personal Hack Days
    - Reinforce management's decision to bestow this privilege
