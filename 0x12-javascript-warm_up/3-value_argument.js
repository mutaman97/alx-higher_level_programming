#!/usr/bin/node
const firstArg = process.argv[2];
if (firstArg) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
