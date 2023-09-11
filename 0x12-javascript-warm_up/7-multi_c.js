#!/usr/bin/node

const s = parseInt(process.argv[2]);
let result;
if (isNaN(s)) {
  result = 'Missing number of occurrences';
  console.log(result);
} else {
  result = 'C is fun';
  let l;
  for (l = 0; l < s; l++) {
    console.log(result);
  }
}
