#!/usr/bin/node

const size = parseInt(process.argv[2]);
let i = 0;
let j = 0;
if (!isNaN(size)) {
  for (i = 0; i < size; i++) {
    let square = '';
    for (j = 0; j < size; j++) {
      square += 'x';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
