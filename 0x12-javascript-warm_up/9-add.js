#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  return a + b;
}

console.log(add(Number(args[2]), Number(args[3])));
