#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  for (let i = 0; i < list.length; i++) {
    revList[i] = list[list.length - i - 1];
  }
  return revList;
};
