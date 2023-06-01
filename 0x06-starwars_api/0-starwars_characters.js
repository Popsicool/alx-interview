#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const id = process.argv[2];

async function main (id) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + id;
  let res = await (await request(endpoint)).body;
  res = JSON.parse(res);
  const char = res.characters;

  for (let i = 0; i < char.length; i++) {
    const urlc = char[i];
    let character = await (await request(urlc)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

main(id);
