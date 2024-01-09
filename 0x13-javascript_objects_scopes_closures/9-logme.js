#!/usr/bin/node
// Write a function that prints the number of arguments already printed and the new argument value
function logMe (item) {
  if (!logMe.count) {
    logMe.count = 0;
  }
  console.log(`${logMe.count}: ${item}`);
  logMe.count++;
}

module.exports.logMe = logMe;
