"""
parent is in pos = 1
left_child = 2*pos 
right_child = 2*pos + 1
parent_of_node = pos // 2

         50
   30         20
 20   10  | 8    16
 
for Heap sort: 
    1- form the element in a max or min heap O(n * log(n))
    2- Delete the elements to sort  O(n * log(n))
Time complexity: O(n*log(n))
Space Complexity: O(1)
"""


def create_max_heap(arr):
    for pos, val in enumerate(arr):
        while pos > 0 and arr[((pos + 1) // 2) - 1] < val:
            arr[((pos + 1) // 2) - 1], arr[pos] = arr[pos], arr[((pos + 1) // 2) - 1]
            pos = ((pos + 1) // 2) - 1
    return arr


def heapSort(arr):
    # create the heap
    arr = create_max_heap(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr = create_max_heap(arr[0: i]) + arr[i: len(arr)]
    return arr

