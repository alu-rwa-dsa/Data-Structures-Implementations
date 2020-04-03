def maxHeapify(arr, len_arr, i):
    f_child = 2 * i + 1
    s_child = 2 * i + 2
    # get the smallest value between the first and second child
    # if first child exists
    if f_child < len_arr:
        largest = f_child
        # if second child exists and less than the first child
        if s_child < len_arr and arr[f_child] < arr[s_child]:
            largest = s_child
        # if the value of the parent is greater than the value of its smallest child
        if arr[i] < arr[largest]:
            # swap the parent with its smallest child
            arr[i], arr[largest] = arr[largest], arr[i]
            # heapify the new sub-tree
            maxHeapify(arr, len_arr, largest)


def heapSort(arr):
    """
    heapSort takes an array of integers, sort it and return the sorted version.
    TimeComplexity: O(n*log(n))
    SpaceComplexity: O(1)
    """
    # create a heap with the given array of integers
    len_arr = len(arr)
    for i in range((len_arr // 2) - 1, -1, -1):
        # maxHeapify takes in the arr, len_arr = len of the array, i = every possible parent
        maxHeapify(arr, len_arr, i)

    # sort the heap by deleting the first element and heapify the rest
    for i in range(len_arr - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, i, 0)
    return arr


