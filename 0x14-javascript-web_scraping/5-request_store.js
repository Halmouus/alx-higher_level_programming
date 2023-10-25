#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
    // console.log(text);
  } else {
    console.error(error);
  }
});
