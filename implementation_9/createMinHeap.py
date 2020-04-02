def min_heapify(arr, len_arr, i):
    parent = (i - 1) // 2
    if arr[i] < arr[i + 1]:
        smallest = i
    else:
        smallest = i + 1

    if arr[parent] < arr[smallest]:
        return arr
    else:
        arr[parent], arr[smallest] = arr[smallest], arr[parent]
        min_heapify(arr, len_arr, (2*smallest) + 1)


def createMinHeap(arr):
    """
    createMinHeap takes an array of integers and swaps elements in place to create a min heap.
    """
    len_arr = len(arr)
    if len_arr % 2 == 0:
        len_arr += 1
    for i in range(len_arr - 2, 0, -2):
        min_heapify(arr, len_arr, i)

    return arr
