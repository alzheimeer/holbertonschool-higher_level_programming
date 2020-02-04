#!/usr/bin/node
//  prints x times “C is fun”

const a = parseInt(process.argv[2]);
if (isNaN(a)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < a; i++) {
    console.log('C is fun');
  }
}
