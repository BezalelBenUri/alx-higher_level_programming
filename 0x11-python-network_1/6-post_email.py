#!/usr/bin/python3
"""  fetches https:  """
import requests
from sys import argv

if __name__ == "__main__":
    email = {'email': argv[2]}
    rd = requests.post(argv[1], data=email)
    print(rd.text)
