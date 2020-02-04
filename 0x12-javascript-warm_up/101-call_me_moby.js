#!/usr/bin/node
exports.callMeMoby = function (a, b) {
  while (a-- > 0) {
    b();
  }
};
