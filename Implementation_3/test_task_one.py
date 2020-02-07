"""
Test all the functions in the Array class
"""
from task_one import Array  # import the array class from task one file
import unittest  # import the unittest module to test the class methods


class TestTaskThree(unittest.TestCase):
    global arr1  # global arr1 object to be accessed across all of the test functions
    arr1 = Array()  # create a global instance of the Array class
    arr1.set(3, 0)  # set values in the array (value, index)
    arr1.set(5, 1)
    arr1.set(10, 2)
    arr1.set(15, 10)  # set the value 15 to index 10, which my algorithm will store in the first empty index (3)

    def test_get(self):
        self.assertEqual(arr1.get(1), 5)  # check if element in index 1 is equal 5

    def test_get2(self):
        self.assertEqual(arr1.get(3), 15)  # check if element in index 3 is equal 15

    def test_len(self):
        self.assertEqual(arr1.len(), 4)  # compare the length of the array to 3


if __name__ == '__main__':
    unittest.main()
