#!/usr/bin/node
// https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Objetos_globales/Array/sort
console.log(process.argv.length < 4 ? 0 : process.argv.slice(2).sort(function (a, b) { return b - a; })[1]);
