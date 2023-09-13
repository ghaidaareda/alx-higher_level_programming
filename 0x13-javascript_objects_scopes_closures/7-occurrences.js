#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const filterdArray = list.filter((current) => current === searchElement);
  return filterdArray.length;
};
