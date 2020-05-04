#!/usr/bin/env python3

# Read lines of text from stdin, reverse it and then print to stdout

from sys import stdin, stderr, exit, exc_info
from textutils import revLine

recordCount = 0

for line in stdin:
    try:
        print(revLine(line))
    except:
        e = exc_info()[0]
        print(f"Could not write output: {e}", file=stderr)
        exit(-1)

    recordCount += 1

stderr.write(f"Processed {recordCount} {'records' if recordCount != 1 else 'record'}\n")
