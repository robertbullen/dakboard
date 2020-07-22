<!-- .slide: id="demos-demos" -->
# Demos

===
<!-- .slide: id="demos-dashboard" -->
## Dashboard

===
<!-- .slide: id="demos-motion-detection" -->
### Motion Detection

===
<form
    class="stretch"
    data-fragment-index="1"
    id="status-url-form"
    style="display: grid; gap: 1rem; grid-template-columns: 1fr auto; grid-template-rows: auto 1fr; place-items: stretch;"
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
        style="align-self: end; max-height: unset; max-width: unset;"
    >
    </video>
</form>
