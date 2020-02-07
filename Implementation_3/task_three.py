"""
Definite the following functions using your dynamic array class as an input. Use only the methods that you have defined
 (len, get, set, add, del) - not built-in methods.
    - contains(array, val) which returns True if val is in the array
    - reverse(array) which reverses the entire array (outputting a new array)
    - insert(array, val, i) which inserts a value at the given index
"""
from task_two import DynamicArray


def contains(array, val):
    """
    Contains function searches for a given value in an array
    :param array: given array instance of the class Dynamic Array
    :param val: given value to look for in the array
    :return: True if the value is in the array, False otherwise
    """
    # looping through the length of the array
    for i in range(array.len()):
        # compare the given value with each of the array values
        if array.get(i) == val:
            # return True if val is found in the array and exit
            return True
    # if no value from the array matched the given value, return False
    return False


def rev(array):
    """
    rev function takes in an array and reverse it
    :param array: given array instance of the class Dynamic Array
    :return: new array that holds all the values in the given array but reversed
    """
    # loop reversely from the length of the array till 0 and add the value of the given array at each index
    # to the new array
    return [array.get(ind) for ind in range(array.len() - 1, -1, -1)]


def insert(array, val, ind):
    """
    ins function takes in an array and value to add to the array at specific index
    :param array: given array instance of the class Dynamic Array
    :param val: value to add to the array
    :param ind: the index in where the value should be added
    :return: the array after adding the value at the given index
    """
    added = False
    new_arr = []
    for i in range(array.len() +1):
        if i == ind:
            new_arr.append(val)
            added = True
        elif added:
            new_arr.append(array.get(i -1))
        else:
            new_arr.append(array.get(i))
    return new_arr
