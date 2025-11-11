#!/usr/bin/node
const { argv } = require('node:process');
const lenargv = argv.length - 2;
if (lenargv === 0) {
  console.log('No argument');
} else if (lenargv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
