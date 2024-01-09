#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
let max = -Infinity;
let secondMax = -Infinity;

args.forEach(num => {
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax && num < max) {
    secondMax = num;
  }
});

console.log(args.length < 2 ? 0 : secondMax);
