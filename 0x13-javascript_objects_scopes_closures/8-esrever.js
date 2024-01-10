#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  for (const element in list) {
    revlist.unshift(element);
  }
  return revlist;
};
