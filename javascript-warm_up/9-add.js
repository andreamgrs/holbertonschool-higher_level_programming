#!/usr/bin/node
const argv1 = process.argv[2];
const num1 = parseInt(argv1, 10);

const argv2 = process.argv[3];
const num2 = parseInt(argv2, 10);

add(num1, num2);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
