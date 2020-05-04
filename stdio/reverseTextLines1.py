#!/usr/bin/env python3

def revLine(line):
    """Reverse the words in a line of text"""
    simpleLine = line.strip()
    words = simpleLine.split()
    revWords = reversed(words)
    newLine = ' '.join(revWords)
    return newLine

# Read lines of text from a file, reverse it and then write to output

from sys import exit

with open("myFile", "r") as infile, \
     open("yourFile", "w") as outfile:

    for line in infile:

        newLine = revLine(line) + "\n" # Text needs "\n"

        try:
            outfile.write(newLine) 
        except:
            pass # Nowhere to write the error!
            exit(-1)
