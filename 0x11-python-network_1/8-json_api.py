#!/usr/bin/python3
""" script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ltr = sys.argv[1]
    else:
        ltr = ""
    pars = {"q": ltr}

    req = requests.post("http://0.0.0.0:5000/search_user", data=pars)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print(f'[{resp.get("id")}] {resp.get("name")}')
    except Exception:
        print("Not a valid JSON")
