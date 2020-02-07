from task_two import DynamicArray
from task_three import *
import unittest  # import the unittest module to test the class methods


class TestTaskThree(unittest.TestCase):
    """
    Test all the functions in the Dynamic array methods
    """
    global arr1  # global arr1 object to be accessed across all of the test functions
    arr1 = DynamicArray()  # create a global instance of the Dynamic array methods class
    arr1.add(3)
    arr1.add(5)
    arr1.add(10)

    def test_reverse(self):
        self.assertEqual(contains(arr1, 3), True)  # check if 3 is in the array == True

    def test_reverser2(self):
        self.assertEqual(contains(arr1, 7), False)  # check if 7 is in the array == False

    def test_insert(self):
        # insert the value 120 in position 0 of the array
        self.assertEqual(insert(arr1, 120, 0), [120, 3, 5, 10])

    def test_rev(self):
        self.assertEqual(rev(arr1), [10, 5, 3, 120])  # reverse the array elements


if __name__ == '__main__':
    unittest.main()

