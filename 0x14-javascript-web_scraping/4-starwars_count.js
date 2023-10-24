#!/usr/bin/node

const request = require('request');

// Check if the API URL argument is provided
if (process.argv.length !== 3) {
  console.error('Usage: node wedge_antilles_movies.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Send a GET request to the Star Wars API to get all films
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const wedgeAntillesMovies = data.results.filter((film) => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(wedgeAntillesMovies.length);
  }
});
