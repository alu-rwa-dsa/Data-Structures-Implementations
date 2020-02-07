"""
Create a simple array class  where each element must be an integer type and:
    - has a .len() method which outputs the length of the array
    - has a .get(i) method which outputs the value at a given index
    - has a a .set(val,i) method which replaces the val at index i
"""


class Array(object):
    def __init__(self, size):
        self.size = size  # define a fixed size of the array
        self.array = [None] * size  # define array field with the value of the given array (arr)
        self._n = 0  # count the number of elements given to the array

    def __str__(self):
        """
        Show the array if the instance variable was printed
        """
        return self.array

    def set(self, val, ind):
        """
        set function takes in a value and index and inserts the given value to the array in the given index
        :param val: given integer value to add to the array
        :param ind: integer represents the index in which the value should be added to the array
        :return: TypeError if the given value is not an int
        """
        if type(val) != int:  # raise type error if value not int type
            raise TypeError
        elif ind > self.size:  # if the given value index greater than the fixed size of the array raise an error
            raise IndexError
        else:
            self._n += 1
            self.array[ind] = val

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
        return self._n


if __name__ == '__main__':
    Array(5)



