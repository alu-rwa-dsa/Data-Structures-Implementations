# time complexity is o(n) where n is the length of the input string because we are looping through every char
# Space complexity is o(n) where n is the length of the string, because n the worst case
# all the chars are unique and every time we will add the new char to the dictionary

from collections import defaultdict


def charOccurrences(string):
    """
    charOccurrences returns a dictionary with the count of every char in the input string
    :param string: user input string contains letters
    :return: a dictionary with the input string unique chars as keys and their number of occurrence as values
    """
    # create an empty dictionary
    d = defaultdict(int)
    # loop through the string
    for char in string:
        d[char] += 1
    return d
