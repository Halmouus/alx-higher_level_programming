#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body);
    for (const char of films.characters) {
      request(char, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const people = JSON.parse(body);
          console.log(people.name);
        } else {
          console.error(error);
        }
      });
    }
  } else {
    console.error(error);
  }
});
