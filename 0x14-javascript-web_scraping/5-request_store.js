#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const body1 = body;
    fs.writeFile(process.argv[3], body1, 'utf-8', (error) => {
      error && console.log(error);
    });
  }
});
