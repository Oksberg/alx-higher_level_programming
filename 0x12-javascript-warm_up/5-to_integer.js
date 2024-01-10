#!/usr/bin/node
const { argv } = require('node:process');
let myNum = Number(argv[2]);

if (myNum) {
  console.log('My number:', myNum);
} else {
  console.log('Not a number');
}
