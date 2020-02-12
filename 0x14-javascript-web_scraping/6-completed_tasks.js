#!/usr/bin/node
const request = require('request');
const options = { // si no colocamos get el lo tom por defecto
  url: process.argv[2],
  method: 'GET'
};
const completed = {};

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const tasks = JSON.parse(body); // body que se convertirá a JSON

  for (const task of tasks) {
    if (task.completed === true) {
      if (!(task.userId in completed)) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  }
  console.log(completed);
});
