#!/usr/bin/node
// concatenates the 2 files passed as arguments
const fs = require('fs');
const A = fs.readFileSync(process.argv[2], 'utf-8');
const B = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], A + B, 'utf-8');
