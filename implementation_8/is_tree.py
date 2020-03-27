"""
Write a function that inputs a list of lists and returns if it can form a tree with the root as the first
element of the list and each other element a subtree.
"""


def isTree(l):
    if type(l[1]) != list:
        for i in l:
            if type(i) == list:
                print(0)


l = [3, [4, [5], [6]], [2, [1], [2]]]
print(isTree(l))
