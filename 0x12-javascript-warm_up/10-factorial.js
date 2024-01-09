#!/usr/bin/node
function factorial (n) {
  return (n > 1) ? n * factorial(n - 1) : 1;
}

const [firstArg] = process.argv.slice(2);
const num = parseInt(firstArg);
console.log(factorial(isNaN(num) ? 1 : num));
