"""
Test all the functions in the Dynamic array class
"""
from task_two import DynamicArray
import unittest  # import the unittest module to test the class methods


class TestTaskThree(unittest.TestCase):
    global arr1  # global arr1 object to be accessed across all of the test functions
    arr1 = DynamicArray()  # create a global instance of the DynamicArray class
    arr1.add(4)  # add the value 4 to the array
    arr1.add(6)

    def test_add(self):
        self.assertEqual(arr1.show(), [4, 6])  # check the array values after adding 4, 5, 6

    def test_delete(self):
        arr1.delete()
        self.assertEqual(arr1.show(), [4])  # check after applying pop, if the last element was deleted

    def test_delete_2(self):
        arr1.delete()  # delete the last element in the array
        with self.assertRaises(IndentationError):  # test for an indexationError if we delete when the arr is empty
            arr1.delete()


if __name__ == '__main__':
    unittest.main()
