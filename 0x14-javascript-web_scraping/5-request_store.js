#!/usr/bin/node
const fs = require('fs');
const reqs = require('request');
reqs(process.argv[2]).pipe(fs.createWriterStream(process.argv[3]));
