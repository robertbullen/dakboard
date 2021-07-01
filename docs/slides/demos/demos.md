<!-- .slide: id="demos-demos" -->
# Demos

===
<!-- .slide: class="columns layout" id="demos-dashboard" -->

<style>
    #demos-dashboard h2 {
        margin-top: 25%;
    }

    #demos-dashboard img {
        border: solid rgba(255, 255, 255, 0.05) 20px;
        max-height: 1000px;
        width: auto;
    }
</style>

<!-- markdownlint-disable first-line-heading heading-start-left -->

- Column

    ## Dashboard

- Column

    ![Dashboard Screenshot](slides/screenshot.png)

<!-- markdownlint-enable first-line-heading heading-start-left -->

===
<!-- .slide: id="demos-motion-detection" -->
## Motion Detection

===
<form
    class="stretch"
    data-fragment-index="1"
    id="status-url-form"
    style="display: grid; gap: 1rem; grid-template-columns: 2fr 1fr; grid-template-rows: auto 1fr; place-items: stretch;"
>
    <input
        id="status-url"
        name="status-url"
        placeholder="Enter the web address to an InterDAKtive webserver"
        style="font-size: x-large;"
        type="url"
    />
    <button
        style="font-size: x-large;"
        type="submit"
    >
        Load Site and Open Webcam
    </button>
    <iframe
        id="status-iframe"
        style="display: block; max-height: unset; max-width: unset;"
    >
    </iframe>
    <video
        autoplay="true"
        id="demo-webcam"
        style="align-self: start; max-height: unset; max-width: unset; transform: scaleX(-1);"
    >
    </video>
</form>
