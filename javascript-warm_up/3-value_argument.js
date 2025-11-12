#!/usr/bin/node
const { argv } = require('node:process');

if (!process.argv[2]) {
  console.log('No argument');
}

argv.forEach((val, index) => {
  if (index === 2) {
    console.log(`${val}`);
  }
  index = index + 1;
});
