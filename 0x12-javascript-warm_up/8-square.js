#!/usr/bin/node

const s = parseInt(process.argv[2]);
if (isNaN(s)) {
  console.log('Missing size');
} else {
  let i, j, string;
  for (i = 0; i < s; i++) {
    string = '';
    for (j = 0; j < s; j++) {
      string += 'X';
    }
    console.log(string);
  }
}
