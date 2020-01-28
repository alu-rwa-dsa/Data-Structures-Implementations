"""
Given a list of lists, return a single list with all of the elements without duplicates
"""

def mergeLists(list_of_lists):
    # create an empty list
    s = set()
    for sub_list in list_of_lists:
        for ele in sub_list:
            s.add(ele)
    # transform the set to a list
    return list(s)


