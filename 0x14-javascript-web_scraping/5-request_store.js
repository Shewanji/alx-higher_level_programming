#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Check if both URL and file path arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: node fetch_and_store_page.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

// Send a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    // Write the response body to the specified file
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
