"""
Input 2 lists - listA with n elements and listB which has all elements of listA except one
(but the rest are in the same order). Outputs the missing element. E.g. f([8,1,2,3],[8,1,3]) outputs 2
"""

def missingElement(l1, l2):
    return (list(set(l1) - set(l2)))[0]

print(missingElement([8, 1, 2, 3], [8, 1, 2]))