#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys

if __name__ == "__main__":
    """impelementation"""
    url = str(sys.argv[1])
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header_value = response.headers.get('X-Request-Id')
        print(header_value)
