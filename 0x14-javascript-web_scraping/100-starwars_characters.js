#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/';
const movie = process.argv[2];

for (let i = 1; i < 10; i++) {
  request(`${url}?page=${i}`, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const people = JSON.parse(body).results;
      for (const charac of people) {
        for (const film of charac.films) {
          if (film.endsWith(`/${movie}/`)) {
            console.log(charac.name);
          }
        }
      }
    } else {
      console.error(error);
    }
  });
}
