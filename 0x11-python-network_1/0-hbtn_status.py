#!/usr/bin/python3
"""get status for a link"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            "https://alx-intranet.hbtn.io/status") as response:
        rd = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(rd)))
        print("\t- content: {}".format(rd))
        print("\t- utf8 content: {}".format(rd.decode("UTF-8")))
