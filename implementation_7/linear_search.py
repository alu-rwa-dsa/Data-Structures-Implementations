def linearSearch(l, target):
    """
    Iterative binary search algorithm
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for val in l:
        if val == target:
            return True
    return False