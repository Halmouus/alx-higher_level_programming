#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const filePath = args[2];
const content = args[3];

fs.writeFile(filePath, content, (err) => {
  if (err) {
    console.error(err);
  }
});
