#!/usr/bin/node

const fs = require('fs');

// Check if both file path and string to write arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node writefile.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file using utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Successfully wrote the string to ${filePath}`);
  }
});
