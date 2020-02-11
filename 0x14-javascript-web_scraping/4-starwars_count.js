#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(body).results;
    let n = 0;
    for (const X of films) {
      for (const char of X) {
        if (char.search('/18/') > 0) {
          n++;
        }
      }
    }
    console.log(n);
  }
});
