# time complexity is o(n) where n is the length of the input string because we are looping through every char
# Space complexity is o(n) where n is the length of the string, because n the worst case
# all the chars are unique and every time we will add the new char to the dictionary


def charOccurrences(string):
    """
    charOccurrences defies an empty dictionary and adds every unique char in the input string
    as a key associated with its number of occurrence as a value
    :param string: user input string contains letters
    :return: a dictionary with the input string unique chars as keys and their number of occurrence as values
    """
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