"""
Create a dynamic array subclass which also has the following basic methods:
    - add(val) which adds an element to the end
    - del() which removes the last element of the list
"""
# import the parent class Array from task_one file
from task_one import Array


# create the DynamicArray as a child class of the parent Array class
class DynamicArray(Array):
    """A dynamic array class is a simple implementation of python's lists"""

    def __init__(self):
        """
        Initializing a static array of size 0
        """
        super().__init__(0)

    def add(self, val):
        """
        add a given value to the end of the array
        :param val: value with any data type to add to the array
        """
        self.array.append(val)
        self._n += 1  # add 1 element to the length of the array

    def delete(self):
        """
        Pops the last element from the array
        """
        if super().len() <= 0:  # if no elements left in the array, raise an index error
            raise IndexError
        else:
            self.array.pop()
            self._n -= 1  # minus 1 element from the length of the array

    def show(self):
        """
        returns the array elements
        """
        return self.array


if __name__ == '__main__':
    arr1 = DynamicArray()

