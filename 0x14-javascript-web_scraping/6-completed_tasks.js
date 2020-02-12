#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed === true) {
        if (!(task.userId in completed)) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    //    console.log(JSON.stringify(completed));
    console.log(completed);
  }
});
