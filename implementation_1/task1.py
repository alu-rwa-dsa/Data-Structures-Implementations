# Time and space calculation of binary search algorithm
import time
import memory_profiler


def binary_search(arr, k):
    """
    Cut the array into halves and look for k
    """
    # pointer0 refers to the index of the first element in the list
    pointer0 = 0
    # pointer1 refers to the index of the last element of the list
    pointer1 = len(arr) - 1
    while pointer0 <= pointer1:
        # mid points to track the middle element of the list
        mid = pointer0 + (pointer1 - pointer0) // 2
        if arr[mid] == k:
            return True
        # if k is greater than the mid number, we move pointer0 to the mid point
        elif arr[mid] < k:
            pointer0 = mid + 1
        # if k is less than the mid number, we move pointer1 to the mid point
        else:
            pointer1 = mid - 1
    return False


# start time point
start = time.perf_counter()

# calling the binary search function and giving it a list of all numbers between 0: 10000
print(binary_search(list(range(10000)), 0))

# end time point
end = time.perf_counter()

# getting the execution time
tot_time = (end - start) / 1000
print("Time it took to run the alg = {} ms".format(tot_time))

# using memory_usage method from memory_profile to accumulate all the space used to run binary_search
mem_usage = memory_profiler.memory_usage(binary_search([1, 2, 3, 4, 5], 0))
print("Total space used = {} MB".format(mem_usage[-1]))
