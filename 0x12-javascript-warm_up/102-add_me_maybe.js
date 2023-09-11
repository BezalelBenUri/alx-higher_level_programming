#!/usr/bin/node

exports.addMeMaybe = function (inst1, callback) {
  inst1 = inst1 + 1;
  callback(inst1);
};
