#!/usr/bin/node
const argv = process.argv;

if (argv[2] && Number(argv[2])) {
  const x = parseInt(argv[2]);
  let row = '';
  for (let i = 0; i < x; i++) {
    row += 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
