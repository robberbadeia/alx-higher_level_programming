#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    """impelementation"""
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, payload)
    try:
        res_dic = response.json()
        if res_dic:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
