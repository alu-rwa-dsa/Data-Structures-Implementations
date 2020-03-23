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
"""


def create_max_heap(arr):
    for pos, val in enumerate(arr):
        while pos > 0 and arr[((pos + 1) // 2) - 1] < val:
            arr[((pos + 1) // 2) - 1], arr[pos] = arr[pos], arr[((pos + 1) // 2) - 1]
            pos = ((pos + 1) // 2) - 1
    return arr


def heap_sort(arr):
    # create the heap
    arr = create_max_heap(arr)
    for i, v in enumerate(arr):
        arr[0], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[0]
        arr[: arr[len(arr) - 1 - i]] = create_max_heap(arr[: arr[len(arr) - 1 - i]])
    return arr


print(heap_sort([30, 20, 10, 40, 50, 3]))
