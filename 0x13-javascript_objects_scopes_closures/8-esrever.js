#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (ar, cut) {
    ar.push(cut);
    return ar;
  }, []);
};
