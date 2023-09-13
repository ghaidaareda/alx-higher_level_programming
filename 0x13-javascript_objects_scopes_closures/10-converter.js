#!/usr/bin/node
exports.converter = function (number, base) {
  let result = '';
  while (number > 0) {
    result = (number % base) + result;
    number = Math.floor(number / base);
  }
  return result;
}
