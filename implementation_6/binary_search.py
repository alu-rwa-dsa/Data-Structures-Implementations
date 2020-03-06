"""
Write a binarySearch(array, val) function that inputs a sorted array/list (ascending order)
and returns if the value is in the array using BinarySearch (should be O(logN) time)
"""


# def binary_search(l, target):
#     """
#     Iterative binary search algorithm
#     """
#     start = 0
#     end = len(l) - 1
#     while start <= end:
#         mid = (end + start) // 2
#         if l[mid] == target:
#             return True
#         elif l[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return False

def binary_search_rec(arr, target, l, r, mid):
    if len(arr) == 0:
        return False
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        r = mid - 1
        return binary_search_rec(arr[l: r+1], target, l, r, (l + r) // 2)
    else:
        arr = arr[mid + 1: r+1]
        r = mid
        return binary_search_rec(arr, target, l, r, (l + r) // 2)


def binarySearch(arr, target):
    """
    binarySearch function takes in an array (arr) and a target values, it returns True if target in arr, False otherwise
    TimeComplexity: O(log(n))
    SpaceComplexity: O(1))
    """
    # intiate the left pointer, right pointer and mid point
    l = 0
    r = len(arr) - 1
    mid = (l + r) // 2
    return binary_search_rec(arr, target, l, r, mid)


