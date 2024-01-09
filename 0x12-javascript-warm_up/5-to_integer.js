#!/usr/bin/node
const [firstArg] = process.argv.slice(2);
const fInt = parseInt(firstArg);

if (isNaN(fInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + fInt);
}
