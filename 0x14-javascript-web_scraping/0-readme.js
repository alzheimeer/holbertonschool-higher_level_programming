#!/usr/bin/node
/* File System Object */
const fs = require('fs');
/* Read File */
try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  process.stdout.write(data);
} catch (e) {
  console.error(e);
}
