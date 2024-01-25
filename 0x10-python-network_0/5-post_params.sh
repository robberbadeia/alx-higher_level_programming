#!/bin/bash
# Take in URL, POST key:vals; Usage: ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
curl -X POST -d "email:hr@holbertonschool.com&subject:I will always be here for PLD" -s "$1"
