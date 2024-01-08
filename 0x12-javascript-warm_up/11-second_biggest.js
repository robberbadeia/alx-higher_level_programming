#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

function secondBigInt (lst) {
  return (lst.sort().reverse()[1]);
}
console.log(secondBigInt(process.argv.slice(2)));
