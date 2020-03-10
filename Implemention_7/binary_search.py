

def search(l, target):
    """
    Iterative binary search algorithm
    """
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (end + start) // 2
        if l[mid] == target:
            return True
        elif l[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False