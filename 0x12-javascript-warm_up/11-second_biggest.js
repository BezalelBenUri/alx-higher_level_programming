#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((m, n) => m - n);
  console.log(args[args.length - 2]);
}
