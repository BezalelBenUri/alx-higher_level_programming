#!/usr/bin/bash
"""  fetches X-Request-Id """
from sys import argv
import requests

if __name__ == __main__:
    requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
