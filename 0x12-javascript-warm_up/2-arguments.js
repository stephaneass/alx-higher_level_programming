#!/usr/bin/node
const args_count = process.argv.length - 2;
console.log(args_count === 0 ? 'No argument' : args_count === 1 ? 'Argument found' : 'Arguments found');
