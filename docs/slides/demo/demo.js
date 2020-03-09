window.addEventListener('load', () => {
	// Reveal's 'ready' event triggers before the form is discoverable and the 'slidechanged'
	// event will not trigger if the browser deep links directly into this slide. Because neither
	// event is 100% reliable, a polling technique is used instead. Once the form is discovered and
	// the 'submit' listener is registered, the polling is cancelled. This polling will likely only
	// occur once or twice.
	const intervalHandle = window.setInterval(() => {
		const statusUrlForm = document.getElementById('status-url-form');
		if (statusUrlForm) {
			window.clearInterval(intervalHandle);

			statusUrlForm.addEventListener('submit', event => {
				event.preventDefault();
				const statusUrl = event.target.elements['status-url'].value;
				document.getElementById('status-iframe').src = statusUrl;
			});
		}
	}, 100);
});
