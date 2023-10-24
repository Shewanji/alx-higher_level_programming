#!/usr/bin/node

const request = require('request');

// Check if the API URL argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: node count_completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Send a GET request to the API to fetch todos
request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
