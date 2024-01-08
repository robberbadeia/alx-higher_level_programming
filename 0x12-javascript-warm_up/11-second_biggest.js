#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

function secondBigInt (lst) {
  if (lst.lenght <= 3) {
    return (0);
  } else {
    return (lst.sort().reverse()[1]);
  }
}
console.log(secondBigInt(process.argv));
