#!/usr/bin/node
const reqs = require('fs');
reqs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
