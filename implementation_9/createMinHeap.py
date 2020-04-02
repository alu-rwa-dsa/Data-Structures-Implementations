def min_heapify(arr, len_arr, i):
    f_child = 2 * i + 1
    s_child = 2 * i + 2
    # get the smallest value between the first and second child
    # if first child exists
    if f_child < len_arr:
        smallest = f_child
        # if second child exists and less than the first child
        if s_child < len_arr and arr[f_child] > arr[s_child]:
            smallest = s_child
        # if the value of the parent is greater than the value of its smallest child
        if arr[i] > arr[smallest]:
            # swap the parent with its smallest child
            arr[i], arr[smallest] = arr[smallest], arr[i]
            # heapify the new sub-tree
            min_heapify(arr, len_arr, smallest)


def createMinHeap(arr):
    """
    createMinHeap takes an array of integers and swaps elements in place to create a min heap.
    TimeComplexity: O(n)
    SpaceComplexity: O(1)
    """
    len_arr = len(arr)
    for i in range((len_arr // 2) - 1, -1, -1):
        # min_heapify takes in the arr, len_arr = len of the array, i = every possible parent
        min_heapify(arr, len_arr, i)

    return arr


print(createMinHeap([3, 17, 20, 12, 10, 1, 2, 6]))
