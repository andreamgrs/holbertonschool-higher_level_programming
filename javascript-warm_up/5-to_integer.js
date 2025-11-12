#!/usr/bin/node
const argv = process.argv[2];
const num = parseInt(argv, 10);

if (process.argv.length > 2) {
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number is: ' + num);
  }
} else {
  console.log('Not a number');
}
