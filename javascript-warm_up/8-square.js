#!/usr/bin/node
const argv = process.argv[2];
const num = parseInt(argv, 10);

if (process.argv.length < 2 || isNaN(num)) {
  console.log('Missing size');
}

for (let col = 0; col < num; col++){
  for (let fil = 0; fil < num; fil++){
    process.stdout.write('x');
  }
  console.log("");
}
