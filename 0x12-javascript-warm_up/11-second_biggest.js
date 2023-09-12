#!/usr/bin/node
if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log('0');
} else {
  process.argv.splice(0, 2);
  process.argv.sort((a, b) => b - a);
  console.log(process.argv[1]);
}
