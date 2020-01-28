"""
Input 2 lists - listA with n elements and listB which has all elements of listA except one (but the
rest are in the same order). Outputs the missing element. E.g. f([8,1,2,3],[8,1,3]) outputs 2
"""


def charOccurrences(string):
    # create an empty dictionary
    d = {}
    # loop through the string
    for char in string:
        # if the char is a key in the dictionary add 1 to its values
        if d.get(char):
            d[char] += 1
        # if it is not a key, then add it as a key with a value of 1
        else:
            d[char] = 1
    return d


print(charOccurrences("mmm ahn 12 a"))
