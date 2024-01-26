#!/usr/bin/python3
"""
Python script that takes in a URL
sends a request to the URL and displays
the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    """impelementation"""
    url = str(sys.argv[1])
    response = requests.get(url)
    if response >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
