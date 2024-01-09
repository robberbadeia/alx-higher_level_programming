#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    }
  }
};
