#!/usr/bin/node
const Square2 = require('./5-square.js');

module.exports = class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    for (; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
