"""
Input 2 lists - listA with n elements and listB which has all elements of listA except one (but the
rest are in the same order). Outputs the missing element. E.g. f([8,1,2,3],[8,1,3]) outputs 2
"""

from collections import Counter

def charOccurrences(string):
    return Counter(string)


def char_occurrences(string):
    d = {}
    for char in string:
        if d.get(char):
            d[char] += 1
        else:
            d[char] = 1
    return d

print(charOccurrences("AhmedAA"))
print(char_occurrences("AhmedAA"))


