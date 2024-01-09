#!/usr/bin/node

const SquareOne = require('./5-square.js');

// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
module.exports = class Square extends SquareOne {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
