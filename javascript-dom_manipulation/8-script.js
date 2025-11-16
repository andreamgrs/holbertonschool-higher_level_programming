document.addEventListener('DOMContentLoaded', () => { // this means when HTML is full load do this, when the browser finish building the DOM tree but before images etc..
  const id = document.querySelector('#hello');
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      id.textContent = data.hello;
    });
});
