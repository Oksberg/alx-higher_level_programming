#!/usr/bin/node

const size = parseInt(process.argv[2]);
let i = 0;
let j = 0;
if (!isNaN(size)) {
  while (i < size) {
    let row = '';
    for (j = 0; j < size; j++) {
      row += 'x';
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
