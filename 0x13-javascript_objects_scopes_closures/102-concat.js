#!/usr/bin/node
const fs = require('fs');

// Grab the file paths from the command line arguments
const [,, fileA, fileB, fileC] = process.argv;

// Read the content of the first file
const contentA = fs.readFileSync(fileA, 'utf8');

// Read the content of the second file
const contentB = fs.readFileSync(fileB, 'utf8');

// Concatenate the contents and write to the destination file
fs.writeFileSync(fileC, contentA + contentB);
