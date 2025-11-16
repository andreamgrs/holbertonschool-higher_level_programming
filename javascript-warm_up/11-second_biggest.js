#!/usr/bin/node
const argv = process.argv[2];
const num = parseInt(argv, 10);

if (process.argv.length <= 2) {
  console.log(0);
  process.exit();
}

if (num === 1 && Number.isNaN(parseInt(process.argv[3], 10))) {
  console.log(0);
  process.exit();
}

let actual, biggest, next;
const numbers = [];
let cont = 2;
biggest = parseInt(process.argv[cont], 10);
while (cont < process.argv.length) {
  actual = parseInt(process.argv[cont], 10);
  numbers.push(actual);
  next = parseInt(process.argv[cont + 1], 10);
  if (actual > biggest) {
    biggest = actual;
  } else if (next > biggest) {
    biggest = next;
  }
  cont++;
}
numbers.sort((a, b) => b - a);
console.log(numbers[1]);
