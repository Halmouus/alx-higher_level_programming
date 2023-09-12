#!/usr/bin/node

const args = process.argv;

if (args.length < 4) {
  console.log(0);
} else {
  let max = Number(args[2]);
  let SecMax = Number(args[3]);
  for (let i = 3; i < args.length; i++) {
    if (Number(args[i]) > max) {
      SecMax = max;
      max = Number(args[i]);
    } else if (Number(args[i]) > SecMax && Number(args[i]) !== max) {
      SecMax = Number(args[i]);
    }
  }
  console.log(SecMax);
}
