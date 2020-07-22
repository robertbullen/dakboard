<!-- .slide: id="design-design" -->
# Design

===
<!-- .slide: id="design-templates" -->
## Existing Templates

- Existing templates are attractive but calendars are either sparse or have small text
- I challenged myself to create a custom design that was both attractive and data-dense

<div class="figures equisized">
    <figure>
        <p><img alt="DAKboard Template 1" src="slides/design/dakboard-agenda-tan.jpg" /></p>
    </figure>
    <figure>
        <p><img alt="DAKboard Template 2" src="slides/design/dakboard-big-calendar.png" /></p>
    </figure>
    <figure>
        <p><img alt="DAKboard Template 3" src="slides/design/dakboard-photo-frame.jpg" /></p>
    </figure>
    <figure>
        <p><img alt="DAKboard Template 4" src="slides/design/dakboard-smarthome-dashboard.jpg" /></p>
    </figure>
</div>

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

    #design-font-candidates > p {
        align-items: center;
        display: flex;
        justify-content: center;
        margin-top: 40px;
        font-size: smaller;
    }

    #design-font-candidates > p > * {
        margin: 0 1rem;
    }

    #design-font-candidates > p > a > * {
        vertical-align: middle;
    }

    #design-font-candidates > p > input {
        width: 25%;
    }
</style>

| Name             | Example                                |                 Numbers                  |                      Letter Forms                       |               Lowercase                |                  Mark Shapes                  |
| ---------------- | -------------------------------------- | :--------------------------------------: | :-----------------------------------------------------: | :------------------------------------: | :-------------------------------------------: |
| Roboto (default) | 11:59 Sun aoce Illiterate Wx Jj rnm O0 |         <abbr title="">🟢</abbr>          |         <abbr title="Narrow apertures">🔴</abbr>         | <abbr title="Medium x-height">🟠</abbr> |            <abbr title="">🟢</abbr>            |
| Montserrat       | 11:59 Sun aoce Illiterate Wx Jj rnm O0 | <abbr title="Variable tracking">🔴</abbr> | <abbr title="Medium apertures; circular bowls">🟠</abbr> |        <abbr title="">🟢</abbr>         |            <abbr title="">🟢</abbr>            |
| Open Sans        | 11:59 Sun aoce Illiterate Wx Jj rnm O0 |         <abbr title="">🟢</abbr>          |                 <abbr title="">🟢</abbr>                 |        <abbr title="">🟢</abbr>         |            <abbr title="">🟢</abbr>            |
| Oxygen           | 11:59 Sun aoce Illiterate Wx Jj rnm O0 | <abbr title="Variable tracking">🔴</abbr> |                 <abbr title="">🟢</abbr>                 |        <abbr title="">🟢</abbr>         | <abbr title="Square tittles & colon">🔴</abbr> |
| Poppins          | 11:59 Sun aoce Illiterate Wx Jj rnm O0 | <abbr title="Variable tracking">🔴</abbr> |         <abbr title="Narrow apertures">🔴</abbr>         |  <abbr title="Single-tier a">🔴</abbr>  |      <abbr title="Square colon">🟠</abbr>      |
| PT Sans          | 11:59 Sun aoce Illiterate Wx Jj rnm O0 |   <abbr title="1 has a foot">🔴</abbr>    |                 <abbr title="">🟢</abbr>                 | <abbr title="Medium x-height">🟠</abbr> |            <abbr title="">🟢</abbr>            |
| Ubuntu           | 11:59 Sun aoce Illiterate Wx Jj rnm O0 |         <abbr title="">🟢</abbr>          |                 <abbr title="">🟢</abbr>                 |        <abbr title="">🟢</abbr>         |            <abbr title="">🟢</abbr>            |

<p>
    <label for="font-scale-range">Grover distance simulator:</label>
    <a href="#" id="font-scale-farther-link">
        <span>Far</span>
        <img alt="Far" src="slides/design/grover-far.jpg" />
    </a>
    <input id="font-scale-range" max="1.0" min="0.1" step="0.1" type="range" value="1.0" />
    <a href="#" id="font-scale-nearer-link">
        <img alt="Near" src="slides/design/grover-near.jpg" />
        <span>Near</span>
    </a>
</p>

===
<!-- .slide: id="design-background-and-colors" -->
## Background and Colors

===
<!-- .slide: class="columns layout" id="design-background" -->
### Background Image and Colors

- Column

    ![Background Image](slides/design/purply-derply-background.jpg)

- Column

    - Looked for an organic, daring background
    - Selected this one from [Unsplash's *Textures & Patterns*](https://unsplash.com/t/textures-patterns)
    - Analyzed its color palette using [Canva's *Color Palette Generator*](https://www.canva.com/colors/color-palette-generator/)

        ![Canva Palette Results](slides/design/purply-derply-canva-palette.png)

    - Chose Medium Violet Red (#8C115C) as the starting point for foreground colors

===
<!-- .slide: class="columns layout" id="design-colors" -->
### Foreground Colors

- Column

    - Kept white as the default foreground text
    - Adopted family conventions for calendar colors&mdash;no legend or names required!
        - Pink for Emily <!-- .element style="color: #f755b7;" -->
        - Orange for Robert <!-- .element style="color: #ffb157;" -->
        - Blue for Brooke <!-- .element style="color: #5bc1f2;" -->
        - Green for Kerry <!-- .element style="color: #c9fd57;" -->
    - Used [paletton.com](https://paletton.com/#uid=758180kl1Wx1x+IcEXDsUWkWEVB) to generate a coherent color palette based off of Medium Violet Red

- Column

    ![Paletton.com Colors](slides/design/paletton-colors.png)

===
<!-- .slide: id="design-layout-and-css" -->
## Layout and CSS

===
<!-- .slide: id="design-layout-to-finished-product" -->
### Initial Layout to Finished Product

<style>
    #design-layout-to-finished-product img {
        height: 800px;
    }
</style>

<div class="figures equisized">
    <figure>
        <p><img alt="Layout Designer" src="slides/design/design-layout.png"></p>
        <figcaption>Layout Designer</figcaption>
    </figure>
    <figure>
        <p><img alt="Raw Result" src="slides/design/design-raw.jpg"></p>
        <figcaption>Raw Result</figcaption>
    </figure>
    <figure>
        <p><img alt="Customized with CSS" src="slides/screenshot.png"></p>
        <figcaption>Customized with CSS</figcaption>
    </figure>
</figures>

===
<!-- .slide: id="design-influence" -->
### Was I Influenced?

<style>
    #design-influence img {
        height: 470px;
        object-fit: cover;
        object-position: 0 100% ;
        width: 784px;
    }
</style>

- After my design was finalized, I realized that it shared similarities with Apple CarPlay
    - Translucent tiles
    - Rounded corners
    - Drop shadows

<div class="figures equisized">
    <figure>
        <p><img alt="Apple CarPlay" src="slides/design/apple-carplay.png"></p>
    </figure>
    <figure>
        <p><img alt="My Design" src="slides/screenshot.png"></p>
    </figure>
</figures>

===
<!-- .slide: data-background-image="slides/design/family-guy-css.gif" data-background-position="center" data-background-size="contain" id="design-css" -->

===
### CSS Calculations and Viewport Units for Infinite Scalability

<pre class="stretch">
    <code
        class="language-css"
        data-line-numbers data-src="https://raw.githubusercontent.com/robertbullen/dakboard/master/css/purply-derply.css"
        data-trim>
    </code>
</pre>

===
### Yields A Consistent Appearance Across Resolutions

<div class="figures equisized">
    <figure>
        <p><img alt="Full HD" src="slides/screenshot.png"></p>
        <figcaption>HD (720×1280)</figcaption>
    </figure>
    <figure>
        <p><img alt="Full HD" src="slides/screenshot.png"></p>
        <figcaption>Full HD (1080×1920)</figcaption>
    </figure>
    <figure>
        <p><img alt="QHD" src="slides/screenshot.png"></p>
        <figcaption>QHD (1440×2560)</figcaption>
    </figure>
    <figure>
        <p><img alt="Full HD" src="slides/screenshot.png"></p>
        <figcaption>UHD/4K (2160×3840)</figcaption>
    </figure>
</figures>
