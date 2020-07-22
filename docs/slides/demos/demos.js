window.addEventListener('load', () => {
	// Reveal's 'ready' event triggers before the form is discoverable and the 'slidechanged'
	// event will not trigger if the browser deep links directly into this slide. Because neither
	// event is 100% reliable, a polling technique is used instead. Once the pertinent elements are
	// obtained and the 'submit' listener is registered, the polling is cancelled. This polling will
	// likely only occur once or twice.
	const intervalHandle = window.setInterval(() => {
		const form = document.getElementById('status-url-form');
		const video = document.getElementById('demo-webcam');

		if (form && video) {
			window.clearInterval(intervalHandle);

			form.addEventListener('submit', (event) => {
				event.preventDefault();

				const input = event.target.elements['status-url'];
				const iframe = document.getElementById('status-iframe');
				iframe.src = input.value;

				if (navigator.mediaDevices.getUserMedia) {
					navigator.mediaDevices
						.getUserMedia({ video: true })
						.then((stream) => (video.srcObject = stream));
				}
			});
		}
	}, 100);
});
