#!/usr/bin/node
// prints My number: <first argument converted in integer>

const n = parseInt(process.argv[2]);
if (isNaN(n)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + n);
}
