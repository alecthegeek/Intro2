#!/usr/bin/env python3

# Read lines of text from stdin, reverse it and then print to stdout

from sys import stderr, exit
from textutils import revLine

while True:
    try:
        line = input()
        print(revLine(line))
    except EOFError:
        exit(0)
    except:
        print("Could not write output", file=stderr)
        exit(-1)
