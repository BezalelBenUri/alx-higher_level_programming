#!/usr/bin/node

const ar = process.argv.slice(2);
const nur = parseInt(ar[0]);
if (isNaN(ar[0])) {
  console.log(1);
} else {
  console.log(factorial(nur));
}
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
