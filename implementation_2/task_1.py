# time complexity is o(1) because re lock up time is constant and doesn't depend on the length of the input
# Space complexity is o(n) where n is the len of the list created using findall function which is basically the number
# of substrings in my initial string. It will be O(n) because I am performing concatenation over the whole list

import re


def deleteWhitespaces(string):
    """
    deleteWhitespaces takes in a string that has substrings that are not well spaced and uses regular
    expressions to extract all the substrings and then concat them with a space
    :param string: user input that contains sub strings separated with many spaces
    :return: the same string well spaces, one space between every two substrings.
    """
    return " ".join(re.findall(r"[a-zA-Z0-9]+", string))
