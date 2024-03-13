#!/usr/bin/node
const numArg = parseInt(process.argv[2]);

if (!isNaN(numArg)) {
  console.log('My number: ' + numArg);
} else {
  console.log('Not a number');
}
