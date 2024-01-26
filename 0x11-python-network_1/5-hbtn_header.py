#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the value
of the variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    """impelementation"""
    url = str(sys.argv[1])
    hsdr_value = requests.get(url).headers.get('X-Request-Id')
    print(hsdr_value)
