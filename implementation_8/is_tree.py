"""
Write a function that inputs a list of lists and returns if it can form a tree with the root as the first
element of the list and each other element a subtree.
"""


def isTree(l):
    if len(l) == 0:
        return True
    else:
        if type(l[0]) == str or type(l[0]) == int:
            pass


l = [3, [4, [5], [6]], [2, [1], [2]]]
print(isTree(l))
