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
    def add(self, val):
        """
        add a given value to the end of the array
        :param val: value with any data type to add to the array
        """
        self.array.append(val)

    def delete(self):
        """
        Pop the last element from the array
        """
        if super().len() <= 0:
            raise IndentationError
        else:
            self.array.pop()

    def show(self):
        """
        returns the array elements
        """
        return self.array


if __name__ == '__main__':
    DynamicArray()

