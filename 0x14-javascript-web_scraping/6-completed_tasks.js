#!/usr/bin/node

const request = require('request');

// Check if the API URL argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: node count_completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Send a GET request to the API to fetch todos
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);

    // Create a map to store the count of completed tasks by user ID
    const completedTaskCountByUser = new Map();

    todos.forEach((task) => {
      if (task.completed) {
        const userId = task.userId;
        if (completedTaskCountByUser.has(userId)) {
          completedTaskCountByUser.set(userId, completedTaskCountByUser.get(userId) + 1);
        } else {
          completedTaskCountByUser.set(userId, 1);
        }
      }
    });

    // Print the users with completed tasks and their respective task counts
    const result = {};
    completedTaskCountByUser.forEach((count, userId) => {
      result[userId] = count;
    });

    console.log(JSON.stringify(result, null, 2));
  }
});
