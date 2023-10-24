#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const filePath = args[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  process.stdout.write(data);
});
