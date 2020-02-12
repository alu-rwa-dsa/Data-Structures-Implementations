# time complexity is o(n) where n is the length of l1
# Space complexity is o(nk) where n is the length of l1 and k is the length of l2


def extraElement(l1, l2):
    """
    return the unique element in l1 which is not in l2
    :param l1: input list 1
    :param l2: input list 2
    :return: the value in l1 which is not in l2
    """
    # get the difference between elements of set1 and set2
    if len(l1) == len(l2):
        return None
    return list(set(l1) - set(l2))[0]


