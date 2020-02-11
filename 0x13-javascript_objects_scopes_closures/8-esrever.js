#!/usr/bin/node
exports.esrever = function (list) {
  const l2 = [];
  for (let i = list.length - 1; i >= 0; i--) {
    l2.push(list[i]);
  }
  return l2;
};
