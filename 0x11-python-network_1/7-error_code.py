#!/usr/bin/python3
"""  fetches https://intranet.hbtn.io/status  """
import requests
from sys import argv

if __name__ == "__main__":
    rd = requests.get(argv[1])
    if rd.status_code >= 400:
        print("Error code: {}".format(rd.status_code))
    else:
        print(rd.text)
