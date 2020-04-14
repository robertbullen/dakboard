window.addEventListener('load', () => {
	const intervalHandle = window.setInterval(() => {
		const fontScaleRange = document.getElementById('font-scale-range');
		if (fontScaleRange) {
			window.clearInterval(intervalHandle);

			fontScaleRange.addEventListener('input', (event) => {
				const fontCells = document.querySelectorAll(
					'#design-font-candidates > table > tbody > tr > td:nth-child(2)',
				);
				for (const fontCell of fontCells) {
					fontCell.style.transform = `scale(${event.target.value})`;
				}
			});
		}
	}, 100);
});
