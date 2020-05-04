#!/usr/bin/env python3

"""
Some text processing functions.

revLine: Reverses the words in a string

"""

def revLine(line):
    """Reverse the words in a line of text.
    
    Let's have some tests to show the function works correctly

    >>> revLine("hello world")
    'world hello'
    
    >>> revLine("hello mars and venus")
    'venus and mars hello'
    
    >>> revLine("hello")
    'hello'
    >>> revLine("")
    ''
    
    """
    words = line.strip().split()
    revWords = reversed(words)
    newLine = ' '.join(revWords)
    return newLine

if __name__ == "__main__":
    import doctest
    doctest.testmod()