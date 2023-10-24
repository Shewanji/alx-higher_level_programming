#!/usr/bin/node

const request = require('request');

// Check if the URL argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: node get_request_status.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

// Send a GET request and display the status code
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
