#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    """impelementation"""
    values = {'email': sys.argv[2]}
    url = str(sys.argv[1])
    hsdr_value = requests.post(url, values)
    print(hsdr_value.text)
