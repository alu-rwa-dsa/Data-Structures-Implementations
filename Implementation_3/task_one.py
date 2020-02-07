"""
Create a simple array class  where each element must be an integer type and:
    - has a .len() method which outputs the length of the array
    - has a .get(i) method which outputs the value at a given index
    - has a a .set(val,i) method which replaces the val at index i
"""


class Array(object):
    def __init__(self):
        self.array = []  # define array field with the value of the given array (arr)

    def set(self, val, ind):
        """
        set function takes in a value and index and inserts the given value to the array in the given index
        :param val: given integer value to add to the array
        :param ind: integer represents the index in which the value should be added to the array
        :return: TypeError if the given value is not an int
        """
        if type(val) != int:  # raise type error if value not int type
            raise TypeError ("Invalid type, not int")
        self.array.insert(ind, val)

    def get(self, ind):
        """
        :param ind: integer represents the needed value's position in the array
        :return: element at index ind
        """
        if not 0 <= ind < len(self.array):
            raise IndexError('Invalid index')
        return self.array[ind]

    def len(self):
        """
        :return: the number of elements in the array
        """
        return len(self.array)


if __name__ == "__main__":
    Array()

