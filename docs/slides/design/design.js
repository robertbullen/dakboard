window.addEventListener('load', () => {
	const intervalHandle = window.setInterval(() => {
		const fartherLink = document.getElementById('font-scale-farther-link');
		const range = document.getElementById('font-scale-range');
		const nearerLink = document.getElementById('font-scale-nearer-link');

		if (fartherLink && range && nearerLink) {
			window.clearInterval(intervalHandle);

			function scaleFontCells() {
				const fontCells = document.querySelectorAll(
					'#design-font-candidates > table > tbody > tr > td:nth-child(2)',
				);
				for (const fontCell of fontCells) {
					fontCell.style.transform = `scale(${range.value})`;
				}
			}

			fartherLink.addEventListener('click', (event) => {
				event.preventDefault();
				range.stepDown();
				scaleFontCells();
			});

			range.addEventListener('input', scaleFontCells);

			nearerLink.addEventListener('click', (event) => {
				event.preventDefault();
				range.stepUp();
				scaleFontCells();
			});
		}
	}, 100);
});
