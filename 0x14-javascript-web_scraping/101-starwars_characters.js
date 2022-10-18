#!/usr/bin/node
const request = require('request');
const film = process.argv[2];
let url = 'http://swapi.co/api/people/';
function filmcharacters (film, url) {
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else if (response.statusCode === 200) {
      let jsonobj = JSON.parse(body);
      let people = jsonobj.results;
      for (let i in people) {
        for (let j in people[i].films) {
          if (people[i].films[j].includes(film)) {
            console.log(people[i].name);
          }
        }
      }
      if (jsonobj.next !== null) {
        filmcharacters(film, jsonobj.next);
      }
    } else {
      console.log('An error occured. Status code: ' + response.statusCode);
    }
  });
}
filmcharacters(film, url);
