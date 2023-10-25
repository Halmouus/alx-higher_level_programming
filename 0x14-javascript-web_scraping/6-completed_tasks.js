#!/usr/bin/node
const request = require('request');

request(process.argv[2], { json: true }, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const done = {};
    for (const task of body) {
      if (task.completed) {
        done[task.userId] = (done[task.userId] || 0) + 1;
      }
    }
    console.log(done);
  } else {
    console.error(error);
  }
});
