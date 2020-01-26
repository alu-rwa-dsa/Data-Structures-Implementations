"""
Input a string of text and output the same text replacing all whitespace with just a single space.
E.g. f(“hello       my        friend”) outputs “hello my friend
"""

def deleteWhitespaces(string):
    return " ".join(string.split())

print(deleteWhitespaces("hello       my        friend"))