#!/usr/bin/node

function factorial (num) {
  num = parseInt(num);

  if (isNaN(num) || num < 0) {
    return (1);
  }
  if (num === 0) {
    return (1);
  }

  return (num * factorial(num - 1));
}

console.log(factorial(process.argv[2]));
