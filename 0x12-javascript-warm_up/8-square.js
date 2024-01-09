#!/usr/bin/node
const [sizeArg] = process.argv.slice(2);
const size = parseInt(sizeArg, 10);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const squareLine = 'X'.repeat(size);
  for (let i = 0; i < size; i++) {
    console.log(squareLine);
  }
}
