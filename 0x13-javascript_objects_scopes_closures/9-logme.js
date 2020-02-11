#!/usr/bin/node
let c = 0;
exports.logMe = function (item) {
  console.log(c + ': ' + item);
  c++;
};
