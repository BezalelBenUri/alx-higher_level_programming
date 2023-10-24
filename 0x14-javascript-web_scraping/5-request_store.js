#!/usr/bin/node
const fs = require('fs');
const reqs = require('request');
reqs(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
