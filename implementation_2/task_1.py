# time complexity is o(1) because re lock up time is constant and doesn't depend on the length of the input
# Space complexity is o(n) where n is the len of the list created using findall function which is basically the number
# of substrings in my initial string. It will be O(n) because I am performing concatenation over the whole list

import re


def delete_whitespaces(s):
    """
    Correct the number of white spaces in a given string (s)
    """
    return " ".join(re.findall(r"[a-zA-Z0-9]+", s))
