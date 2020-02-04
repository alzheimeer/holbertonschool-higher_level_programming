#!/usr/bin/node
// prints a square

const a = parseInt(process.argv[2]);

if (isNaN(a)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < a; i++) {
    console.log('X'.repeat(a));
  }
}
