#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const [firstArg, secondArg] = process.argv.slice(2);
const firstInt = parseInt(firstArg);
const secondInt = parseInt(secondArg);

console.log(add(firstInt, secondInt));
