#!/usr/bin/node

const args = process.argv;

if (isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  const size = Number(args[2]);
  if (size >= 0) {
    const square = 'X'.repeat(size);
    for (let i = 0; i < size; i++) { console.log(square); }
  }
}
