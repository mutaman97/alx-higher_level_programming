#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    // If c is undefined, use 'X' as the character
    if (c === undefined) {
      c = 'X';
    }
    console.log((c.repeat(this.width) + '\n').repeat(this.height));
  }
}

module.exports = Square;
