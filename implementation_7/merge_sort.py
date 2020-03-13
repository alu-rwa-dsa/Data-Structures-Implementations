def innerSort(left, right):
    res = []
    l_pointer = r_pointer = 0

    while l_pointer < len(left) and r_pointer < len(right):
        if left[l_pointer] < right[r_pointer]:
            res.append(left[l_pointer])
            l_pointer += 1
        else:
            res.append(right[r_pointer])
            r_pointer += 1

    res.extend(right[r_pointer:])
    res.extend(left[l_pointer:])
    return res


def mergeSort(arr):
    """
    mergeSort takes in an array and returns it, sorted.
    """
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    left, right = mergeSort(arr[:midpoint]), mergeSort(arr[midpoint:])
    return innerSort(left, right)


array = [4, 4, 3, 2, 1, 6, 7, 8]
result = mergeSort(array)
print(result)
