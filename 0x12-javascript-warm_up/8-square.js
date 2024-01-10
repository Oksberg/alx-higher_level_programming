#!/usr/bin/node
const { argv } = require('node:process');
const size = Number(argv[2]);
let i = 0;
let row = '';

if (size) {
  for (let j = 0; j < size; j++) {
    row += 'x';
  }

  for (let i = 0; i < size; i++)
  console.log(row);

} else {
  console.log('Missing size');
}
