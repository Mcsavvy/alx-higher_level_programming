#!/usr/bin/node

const Base = require('./5-square.js');

class Square extends Base {
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
