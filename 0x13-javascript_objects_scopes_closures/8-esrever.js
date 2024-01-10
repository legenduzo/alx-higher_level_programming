#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  for (const element of list) {
    revlist.unshift(element);
  }
  return revlist;
};
