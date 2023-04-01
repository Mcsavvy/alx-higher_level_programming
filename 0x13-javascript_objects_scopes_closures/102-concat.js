#!/usr/bin/node

const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, (err, data) => {
  if (err) { throw err; }
  const contentFileA = data.toString();
  fs.writeFile(fileC, contentFileA, () => {});
});

fs.readFile(fileB, (err, data) => {
  if (err) { throw err; }
  const contentFileB = data.toString();
  fs.appendFile(fileC, contentFileB, () => {});
});
