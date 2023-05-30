#!/usr/bin/node

// Star Wars Characters
const request = require('request');
const num = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${num}`
const url2 = "https://swapi-api.alx-tools.com/api/people/"

request(url, function(error, response, body){
    const char = JSON.parse(body)["characters"]
    char.forEach(element => {
        const el = parseInt(element.split("/").slice(-2, -1).toString())
        request(`${url2 + el}`, function(error2, response2, body2){
            const name = JSON.parse(body2)["name"]
            console.log(name)
        })
    });
})

function getUser(url){
}