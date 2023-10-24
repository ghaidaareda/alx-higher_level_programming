#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];
const str = process.argv[3];
fs.writeFile(fileName, str, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
