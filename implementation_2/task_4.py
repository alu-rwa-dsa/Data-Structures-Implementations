"""
Input 2 lists - listA with n elements and listB which has all elements of listA except one
(but the rest are in the same order). Outputs the missing element. E.g. f([8,1,2,3],[8,1,3]) outputs 2
"""


def extraElement(l1, l2):
    # get the difference between elements of set1 and set2
    if len(l1) == len(l2):
        return None
    return list(set(l1) - set(l2))[0]


