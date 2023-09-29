#!/usr/bin/python3
"""  fetches X-Request-Id """
import requests
from sys import argv

if __name__ == "__main__":
    rd = requests.get(argv[1])
    print(rd.headers.get('X-Request-Id'))
