"""
Write a function that inputs a list of lists and returns if it can form a tree with the root as the first
element of the list and each other element a subtree.
"""


def isTree(l, value=True):
    if len(l) == 0:
        return True
    if len(l) == 1:
        return type(l[0]) != list
    if type(l[0]) != list:
        for ele in l[1:]:
            if type(ele) != list:
                return False
            value = isTree(ele)
    else:
        return False

    return value


