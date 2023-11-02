#!/usr/bin/node
$.get('https://swapi.co/api/films/?format=json', function (data) {
  for (const film of data.results) {
    $('#list_movies').append(`<li>${film.title}</li>`);
  }
});