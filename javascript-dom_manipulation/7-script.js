const ul = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(element => { //each element look like { tittle: .. number:...}
      const newItemOnList = document.createElement('li');
      newItemOnList.textContent = element.title;
      ul.appendChild(newItemOnList);
    });
  });
