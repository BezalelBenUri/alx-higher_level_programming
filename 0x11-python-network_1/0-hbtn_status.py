#!/usr/bin/python3
"""Fetches status of link"""
import urllib

if __name__ == "__main__":
    request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urlib.request.urlopen(request) as response:
        body = response.read()
        print("Response:")
        print"\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
