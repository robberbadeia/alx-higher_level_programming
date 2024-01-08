#!/usr/bin/node
// script that prints the addition of 2 integers
function add (a, b) {
  const sum = (a - 0) + (b - 0);
  return (sum);
}

if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log('Not a number');
} else {
  console.log(add(process.argv[2], process.argv[3]));
}
