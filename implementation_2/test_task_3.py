import unittest
from implementation_2.task_3 import mergeLists


class Test(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(mergeLists([[1, 2, 3], [4, 5]]), [1, 2, 3, 4, 5])

    def testCase2(self):
        self.assertEqual(mergeLists([[1, 2, 3], [0, 1, 2, 3]]), [0, 1, 2, 3])

    def testCase3(self):
        self.assertEqual(mergeLists([[1], [5], [1]]), [1, 5])

    def testCase4(self):
        self.assertEqual(mergeLists([[3]]), [3])


if __name__ == "__main__":
    Test()
