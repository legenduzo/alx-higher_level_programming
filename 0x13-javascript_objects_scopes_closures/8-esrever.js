#!/usr/bin/node

exports.esrever = function (list) {
  let revlist = [];
  for (const element of list) {
    revlist.unshift(element);
  }
  return revlist;
};
