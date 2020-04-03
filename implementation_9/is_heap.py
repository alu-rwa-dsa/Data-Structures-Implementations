def isMinHeap(arr):
    """
    isMinHeap takes in an array and returns True if it represents a min heap or False otherwise
    TimeComplexity: O(log(n)) for looping through half of the list
    SpaceComplexity: O(1)
    """
    if len(arr) == 0:
        return False
    for i in range(len(arr)//2):
        # check if the node has 2 children
        if (2 * i + 2) < len(arr):
            if arr[i] > arr[2 * i + 1] or arr[i] > arr[2 * i + 2]:
                return False
        else:
            return arr[i] <= arr[2 * i + 1]
    return True


