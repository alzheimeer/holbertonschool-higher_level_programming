#!/usr/bin/node
// prints a square

const a = parseInt(process.argv[2]);

if (isNaN(a)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < a; i++) {
    console.log('X'.repeat(a));
  }
}
