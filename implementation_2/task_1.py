"""
Input a string of text and output the same text replacing all whitespace with just a single space.
E.g. f(“hello       my        friend”) outputs “hello my friend
"""
import re


def deleteWhitespaces(string):
    # using regular expressions to find all of the matched pieces of the string
    # use the join to merge the list elements into a string
    return " ".join(re.findall(r"[a-zA-Z0-9]+", string))