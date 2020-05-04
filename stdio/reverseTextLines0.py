#!/usr/bin/env python3

def revLine(line):
    """Reverse the words in a line of text"""
    words = line.split()
    revWords = reversed(words)
    newLine = ' '.join(revWords)
    return newLine

# Read one line of text from keyboard, reverse it and then print to screen

line = input("Please type in line of text : ")

newLine = revLine(line)

print(newLine)
