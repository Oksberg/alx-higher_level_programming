#!/usr/bin/node

const numArg = parseInt(process.argv[2]);
let i = 0;
if (!isNaN(numArg)) {
  while (i < numArg) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
