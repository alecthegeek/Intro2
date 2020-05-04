#!/usr/bin/env python3

import subprocess
from requests import get
from bottle import template, route, request, run
from sys import stderr, exit
from dumper import dump

page = """
{{displayText}}

<form action="/" method="GET">
    <input type="submit" name="getnewcontent" value="getnewcontent">
    <input type="submit" name="transformcontent" value="transformcontent">
</form>
"""

def processText(text):
    print("transforming text", file=stderr)
    inputb = bytearray(text,"utf-8")
    resp = subprocess.run(["./reverseTextLines2.py"], shell=True, input= inputb, capture_output= True)
    return resp.stdout.decode("utf-8")

@route('/')
def swapText(method="GET"):
    if not hasattr(swapText, "displayText"): # 1st time -- get some text
        swapText.displayText = get("https://loripsum.net/api/5/short/plaintext").text
        print("Initialised display text", file=stderr)

    elif request.query.getnewcontent == "getnewcontent":
        swapText.displayText = get("https://loripsum.net/api/5/short/plaintext").text
        print("Re initialised display text", file=stderr)

    elif request.query.transformcontent == "transformcontent":
        swapText.displayText = processText(swapText.displayText)
        print("Processed text", file=stderr)

    else:
        print("Unknown response", file=stderr)
        exit(-1)

    return template(page, displayText=swapText.displayText)
    
if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)