#!/usr/bin/node
const argv = process.argv[2];
const num = parseInt(argv, 10);

if (process.argv.length <= 2) {
  console.log(1);
  process.exit();
}

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(num));
