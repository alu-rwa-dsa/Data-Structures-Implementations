def bubbleSort(arr):
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
