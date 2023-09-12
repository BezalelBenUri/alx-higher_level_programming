#!/usr/bin/node

const sc = require('fs');
const a = sc.readFileSync(process.argv[2], 'utf8');
const b = sc.readFileSync(process.argv[3], 'utf8');
sc.writeFileSync(process.argv[4], a + b);
