#!/usr/bin/python3
"""https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    rd = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(rd.text)))
    print("\t- content: {}".format(rd.text))
