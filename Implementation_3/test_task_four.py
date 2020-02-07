"""
Test all the functions in the AssociativeList class
"""
from task_four import AssociativeList
import unittest  # import the unittest module to test the class methods


class TestTaskThree(unittest.TestCase):
    global d1  # global d1 object to be accessed across all of the test functions
    d1 = AssociativeList()

    def test_add(self):
        global d1
        d1.add("Ahmed", 12)
        d1.add("Arun", 1)
        self.assertEqual(d1.lookUp("Ahmed"), 12)  # check the value of the key Ahmed == 12

    def test_add2(self):
        global d1
        self.assertEqual(d1.lookUp("Khal"), None)  # check if the value of a None existing key is None

    def test_remove(self):
        global d1
        d1.remove("Arun")
        self.assertEqual(d1.lookUp("Arun"), None)  # check if the value of Arun after deleting it is None

    def test_remove2(self):
        global d1
        with self.assertRaises(KeyError):  # test for a None existing key
            d1.remove("Arun")

    def test_modify(self):
        global d1
        d1.modify("Ahmed", 120)
        self.assertEqual(d1.lookUp("Ahmed"), 120)  # check the value of the key Ahmed is updated to 120


if __name__ == '__main__':
    unittest.main()
