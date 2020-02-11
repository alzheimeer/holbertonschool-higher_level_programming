#!/usr/bin/node
/* change base and make closures */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
