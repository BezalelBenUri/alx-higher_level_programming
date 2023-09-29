#!/usr/bin/python3
"""  fetches https..."""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        info = {"q": argv[1]}
    else:
        info = {"q": ""}
    rd = requests.post("http://0.0.0.0:5000/search_user", data=info)
    try:
        if rd.json() == {}:
            print("No result")
        else:
            print("[{}] ".format(rd.json().get("id")), end="")
            print(rd.json().get("name"))
    except:
        print("Not a valid JSON")
