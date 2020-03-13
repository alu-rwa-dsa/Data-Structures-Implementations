def bubbleSort(arr):
    """
    bubbleSort takes in an array and returns it in a sorted format
    Time Complexity: Best case O(n), Average Case: O(n*log(n), Worst case: O(n**2))
    Space Complexity: O(1)
    """
    trigger = True
    arr_len = len(arr) - 1
    while arr_len > 0 and trigger:
        trigger = False
        for i in range(arr_len):
            if arr[i] > arr[i + 1]:
                trigger = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        arr_len -= 1
    return arr


print(bubbleSort([2, 3, 5, 1, 0]))
