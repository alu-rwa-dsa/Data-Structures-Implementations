import unittest
from implementation_2.task_5 import listCounter, listCounter2


class Test(unittest.TestCase):
    """
    Test class tests different possible string inputs to deleteWhitespaces against there expected output
    if the function output matches the expected given output; return Ok
    """
    def testCase1(self):
        self.assertEqual(listCounter(2), [1, 2, 2])

    def testCase2(self):
        self.assertEqual(listCounter(3), [1, 2, 2, 3, 3, 3])

    def testCase3(self):
        self.assertEqual(listCounter(0), [])

    def testCase4(self):
        self.assertEqual(listCounter2(2), [1, 2, 2])

    def testCase5(self):
        self.assertEqual(listCounter2(3), [1, 2, 2, 3, 3, 3])

    def testCase6(self):
        self.assertEqual(listCounter2(0), [])


if __name__ == "__main__":
    Test()