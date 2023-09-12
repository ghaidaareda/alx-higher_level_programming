#!/usr/bin/node
function add (a, b) {
  const c = a + b;
  console.log(c);
}
a = parseInt(process.argv[2]);
b = parseInt(process.argv[3]);
add(a, b);
