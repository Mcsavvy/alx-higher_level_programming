#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let x = 0; x < this.height; x++) {
      console.log(Array(this.width + 1).join(c || 'X'));
    }
  }
}

module.exports = Square;
