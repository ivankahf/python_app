lightbox.option({
  'resizeDuration': 200,
  'wrapAround': true
});

const lightbox = document.querySelector('#lightbox');
const backBtn = document.querySelector('#back-btn');

backBtn.addEventListener('click', () => {
  lightbox.style.display = 'none';
});