# time complexity is o(n.m) where n is the length of list and m is the length of the longest sub lists
# Space complexity is o(k) where k is the length of all unique elements in the list of lists


def mergeLists(list_of_lists):
    """
    mergeLists takes in a list of lists and returns one list with all of the unique values of the given list_of_lists.
    :param list_of_lists: a lists with number of sub lists
    :return: one list with all of the unique values in the sub lists of list_of_lists.
    """
    # create an empty set
    s = set()
    for sub_list in list_of_lists:
        # add the elements of teh sublist to the set
        for ele in sub_list:
            s.add(ele)
    # transform the set to a list
    return list(s)
