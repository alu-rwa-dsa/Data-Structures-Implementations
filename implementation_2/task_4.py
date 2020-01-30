# time complexity is o(n) where n is the length of l1
# Space complexity is o(1) because we are not initializing any new arrays


def extraElement(l1, l2):
    """
    extraElement takes in two lists, l1 has one extra element compared to l2, it loos through l1 and
    checks if the element is in l2, and if it is not, it returns the element
    :param l1: input list 1
    :param l2: input list 2
    :return: the value in l1 which is not in l2
    """
    # get the difference between elements of set1 and set2
    if len(l1) == len(l2):
        return None
    return list(set(l1) - set(l2))[0]


