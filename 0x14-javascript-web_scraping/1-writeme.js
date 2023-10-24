#!/usr/bin/node
const reqs = require('fs');
reqs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
