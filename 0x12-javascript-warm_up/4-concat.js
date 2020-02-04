#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

const a = process.argv[2];
const b = process.argv[3];

console.log(`${a} is ${b}`);
