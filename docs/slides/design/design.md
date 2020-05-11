<!-- .slide: id="design-design" -->
# Design

===
<!-- .slide: id="design-templates" -->
## Existing Templates

- Existing templates were attractive but sparse
- Challenge: create a custom design that was both attractive and data-dense

<div class="figures equisized">
    <figure>
        <img alt="DAKboard Template 1" src="slides/design/dakboard-agenda-tan.jpg" />
    </figure>
    <figure>
        <img alt="DAKboard Template 2" src="slides/design/dakboard-big-calendar.png" />
    </figure>
    <figure>
        <img alt="DAKboard Template 3" src="slides/design/dakboard-photo-frame.jpg" />
    </figure>
    <figure>
        <img alt="DAKboard Template 4" src="slides/design/dakboard-smarthome-dashboard.jpg" />
    </figure>
</div>

===
<!-- .slide: class="columns layout" id="design-background" -->
## Background Image and Colors

- Column

    ![Background Image](slides/design/purply-derply-background.jpg)

- Column

    - I started with this background, which was selected from [Unsplash's *Textures & Patterns*](https://unsplash.com/t/textures-patterns)
    - I was looking for a natural yet daring background
    - Ran it through [Canva's *Color Palette Generator*](https://www.canva.com/colors/color-palette-generator/), which analyzed the image and came up with the following five colors

        ![Canva Palette Results](slides/design/purply-derply-canva-palette.png)

    - I chose Medium Violet Red (#8C145C) as my starting point for the color palette

===
<!-- .slide: class="columns layout" id="design-colors" -->
## Foreground Colors

- Column

    - White as default foreground text
    - Preassigned colors for calendars (no legend or names required!)
        - Pink for Emily
        - Orange for Robert
        - Blue for Brooke
        - Green for Kerry
    - Used [paletton.com](https://paletton.com/#uid=758180kl1Wx1x+IcEXDsUWkWEVB) to select the following

- Column

    ![Paletton.com Colors](slides/design/paletton-colors.png)

===
<!-- .slide: id="design-font" -->
## Font

===
<!-- .slide: id="design-font-criteria" -->
### Font Selection Criteria

<style>
    #design-font-criteria .figures {
        font-size: smaller;
    }

    #design-font-criteria .figures img {
        height: auto;
        width: 220px;
    }

    #design-font-criteria .figures figcaption {
        font-size: smaller;
    }
</style>

<div class="figures">
    <figure class="fragment">
        <h4>Availability</h4>
        <p>
            <img alt="Google Fonts Logo" src="slides/design/google-fonts-logo.png" />
        </p>
        <figcaption>fonts.google.com</figcaption>
    </figure>
    <figure class="fragment">
        <h4>Features</h4>
        <p>
            <img alt="Sans-Serif" src="slides/design/font-anatomy/sans-serif.png" />
            <img alt="Weight" src="slides/design/font-anatomy/weights.png" />
        </p>
        <figcaption class="small">Sans serif; Normal & light weights</figcaption>
    </figure>
    <figure class="fragment">
        <h4>Numbers</h4>
        <p>
            <img alt="Tracking" src="slides/design/font-anatomy/tracking.png" />
            <img alt="Ear" src="slides/design/font-anatomy/ear.png" />
            <img alt="Foot" src="slides/design/font-anatomy/foot.png" />
        </p>
        <figcaption>Invariant tracking, <em>1</em> with an ear but no foot</figcaption>
    </figure>
    <figure class="fragment">
        <h4>Letter Forms</h4>
        <p>
            <img alt="Counter" src="slides/design/font-anatomy/counter.png" />
            <img alt="Aperture" src="slides/design/font-anatomy/aperture.png" />
            <img alt="Bowl" src="slides/design/font-anatomy/bowl.png" />
        </p>
        <figcaption>Large counters & apertures; tall oval bowls</figcaption>
    </figure>
    <figure class="fragment">
        <h4>Lowercase</h4>
        <p>
            <img alt="X-height" src="slides/design/font-anatomy/x-height.png" />
            <img alt="Tiers" src="slides/design/font-anatomy/tiers.png" />
        </p>
        <figcaption>Tall x-height & two-tiered <em>a</em></figcaption>
    </figure>
    <figure class="fragment">
        <h4>Mark Shapes</h4>
        <p>
            <img alt="Terminal" src="slides/design/font-anatomy/terminal.png" />
            <img alt="Tittle" src="slides/design/font-anatomy/tittle.png" />
        </p>
        <figcaption>Angular terminals; circular <em>:</em> & tittles</figcaption>
    </figure>
</div>
<p>Graphics from <a href="https://www.fontsmith.com/blog/2016/06/29/the-a-z-of-typographic-terms">Fontsmith's <cite>The A-Z of Typographic Terms</cite></a>.</p>

===
<!-- .slide: id="design-font-candidates" -->
### Font Candidates

<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Oxygen&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=PT+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');

    #design-font-candidates > table > thead > tr > th:nth-child(3),
    #design-font-candidates > table > thead > tr > th:nth-child(4),
    #design-font-candidates > table > thead > tr > th:nth-child(5),
    #design-font-candidates > table > thead > tr > th:nth-child(6) {
        font-size: smaller;
        transform: rotate(-45deg);
        max-width: 42px;
        min-width: 42px;
        white-space: nowrap;
    }

    #design-font-candidates > table > tbody > tr > td:nth-child(2) {
        font-size: larger;
    }
    #design-font-candidates > table > tbody > tr > td:nth-child(1n+3) {
        font-size: smaller;
        vertical-align: middle;
    }

    #design-font-candidates > table > tbody > tr > td abbr {
        text-decoration: none;
    }

    #design-font-candidates > table > tbody > tr:nth-child(1) > td:nth-child(2) {
        font-family: 'Roboto';
    }

    #design-font-candidates > table > tbody > tr:nth-child(2) > td:nth-child(2) {
        font-family: 'Montserrat';
    }

    #design-font-candidates > table > tbody > tr:nth-child(3) > td:nth-child(2) {
        font-family: 'Open Sans';
    }

    #design-font-candidates > table > tbody > tr:nth-child(4) > td:nth-child(2) {
        font-family: 'Oxygen';
    }

    #design-font-candidates > table > tbody > tr:nth-child(5) > td:nth-child(2) {
        font-family: 'Poppins';
    }

    #design-font-candidates > table > tbody > tr:nth-child(6) > td:nth-child(2) {
        font-family: 'PT Sans';
    }

    #design-font-candidates > table > tbody > tr:nth-child(7) > td:nth-child(2) {
        font-family: 'Ubuntu';
    }
</style>

| Name             | Example                                |                 Numbers                  |                      Letter Forms                       |               Lowercase                |                  Mark Shapes                  |
| ---------------- | -------------------------------------- | :--------------------------------------: | :-----------------------------------------------------: | :------------------------------------: | :-------------------------------------------: |
| Roboto (default) | 11:59 Sun aoce Illiterate xN Jj rnm O0 |         <abbr title="">🟢</abbr>          |         <abbr title="Narrow apertures">🔴</abbr>         | <abbr title="Medium x-height">🟠</abbr> |            <abbr title="">🟢</abbr>            |
| Montserrat       | 11:59 Sun aoce Illiterate xN Jj rnm O0 | <abbr title="Variable tracking">🔴</abbr> | <abbr title="Medium apertures; circular bowls">🟠</abbr> |        <abbr title="">🟢</abbr>         |            <abbr title="">🟢</abbr>            |
| Open Sans        | 11:59 Sun aoce Illiterate xN Jj rnm O0 |         <abbr title="">🟢</abbr>          |                 <abbr title="">🟢</abbr>                 |        <abbr title="">🟢</abbr>         |            <abbr title="">🟢</abbr>            |
| Oxygen           | 11:59 Sun aoce Illiterate xN Jj rnm O0 | <abbr title="Variable tracking">🔴</abbr> |                 <abbr title="">🟢</abbr>                 |        <abbr title="">🟢</abbr>         | <abbr title="Square tittles & colon">🔴</abbr> |
| Poppins          | 11:59 Sun aoce Illiterate xN Jj rnm O0 | <abbr title="Variable tracking">🔴</abbr> |         <abbr title="Narrow apertures">🔴</abbr>         |  <abbr title="Single-tier a">🔴</abbr>  |      <abbr title="Square colon">🟠</abbr>      |
| PT Sans          | 11:59 Sun aoce Illiterate xN Jj rnm O0 |   <abbr title="1 has a foot">🔴</abbr>    |                 <abbr title="">🟢</abbr>                 | <abbr title="Short x-height">🔴</abbr>  |            <abbr title="">🟢</abbr>            |
| Ubuntu           | 11:59 Sun aoce Illiterate xN Jj rnm O0 |         <abbr title="">🟢</abbr>          |                 <abbr title="">🟢</abbr>                 |        <abbr title="">🟢</abbr>         |            <abbr title="">🟢</abbr>            |

<input id="font-scale-range" max="1.0" min="0.2" step="0.2" type="range" value="1.0" />

===
<!-- .slide: data-background-image="slides/design/family-guy-css.gif" data-background-position="center" data-background-size="contain" id="design-css" -->
