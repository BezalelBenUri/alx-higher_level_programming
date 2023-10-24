#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const dos = JSON.parse(body);
    const completed = {};
    dos.forEach((tod) => {
      if (tod.completed && completed[tod.userId] === undefined) {
        completed[tod.userId] = 1;
      } else if (tod.completed) {
        completed[tod.userId] += 1;
      }
    });
    console.log(completed);
  }
});
