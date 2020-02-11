#!/usr/bin/node
var https = require('https');
const request = https.get(process.argv[2], function (response) {
  console.log(response.statusCode);
});

request.on('error', function (error) {
  console.error(error.status);
});
