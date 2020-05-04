#!/usr/bin/env python3

# Read lines of text from stdin, reverse it and then write to stdout
# Write error messages to stderr

# See https://en.wikipedia.org/wiki/Standard_streams

from sys import stdin, stdout, stderr, exit, exc_info
from textutils import revLine

recordCount = 0

for line in stdin:

    newLine = revLine(line) + "\n" # Text needs "\n"

    try:
        stdout.write(newLine)
    except:
        e = exc_info()[0]
        stderr.write(f"Could not write output: {e}\n")
        exit(-1)

    recordCount += 1

stderr.write(f"Processed {recordCount} {'records' if recordCount != 1 else 'record'}\n")
