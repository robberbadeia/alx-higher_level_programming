#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -s "$1" -X POST -H "email: test@gmail.com" -H "subject:I will always be here for PLD"
