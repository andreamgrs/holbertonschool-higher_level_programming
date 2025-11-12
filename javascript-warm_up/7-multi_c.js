#!/usr/bin/node
const argv = process.argv[2];
const num = parseInt(argv, 10);
let cont = 0;

if (process.argv.length < 2) {
  console.log('Missing number of occurrences');
}

while (cont < num) {
  console.log('C is fun');
  cont++;
}
