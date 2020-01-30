# time complexity is o((1+sqrt(1 + 8*n)) / 2) where n is the length of range(number)
# Space complexity is o(n.k) where n is the length of range(number) and k is the length of sub list of n


def listCounter(num):
    """
    listCounter takes in a number and loops through the range of that number and adds every element n, n times
    to the output list.
    :param num: input number to loop through its range
    :return: a list with all elements in range(num) repeated n times
    """
    return [i for i in range(1, num+1) for _ in range(i)]


def listCounter2(num):
    l = []
    for i in range(1, num+1):
        l.extend([i] * i)
    return l

