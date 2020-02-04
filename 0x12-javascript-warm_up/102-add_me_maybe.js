#!/usr/bin/node
exports.addMeMaybe = function (a, b) {
  return b(a + 1);
};
