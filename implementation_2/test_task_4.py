import unittest
from task_4 import extraElement

class Test(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(extraElement([1, 2, 3, 4], [1, 2, 3]), 4)

    def testCase2(self):
        self.assertEqual(extraElement([], []), None)

    def testCase3(self):
        self.assertEqual(extraElement([1, 2, 3, 3], [1, 2]), 3)


if __name__ == "__main__":
    Test()