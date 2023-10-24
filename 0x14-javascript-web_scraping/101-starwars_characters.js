#!/usr/bin/node
const reqs = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function printChar (characters, idx) {
  reqs(characters[idx], (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printChar(characters, idx + 1);
      }
    }
  });
}

reqs(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    printChar(characters, 0);
  }
});
