#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""
import sys
import requests


if __name__ == "__main__":
    rd = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
     commits = rd.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
