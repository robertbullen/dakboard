window.addEventListener('load', () => {
	const intervalHandle = window.setInterval(() => {
		const dataSrcAttr = 'data-src';
		const codes = document.querySelectorAll(
			`pre > code.hljs[${dataSrcAttr}]`,
		);
		if (codes.length > 0) {
			window.clearInterval(intervalHandle);

			highlightPlugin = Reveal.getPlugin('highlight');
			codes.forEach(async (code) => {
				const response = await fetch(code.dataset.src);
				if (response.ok) {
					code.textContent = await response.text();
					highlightPlugin.highlightBlock(code);
				}
			});
		}
	}, 100);
});
