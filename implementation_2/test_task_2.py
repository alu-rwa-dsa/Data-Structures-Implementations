import unittest
from implementation_2.task_2 import charOccurrences


class Test(unittest.TestCase):
    """
    Test class tests different possible string inputs to deleteWhitespaces against there expected output
    if the function output matches the expected given output; return Ok
    """
    def testCase1(self):
        self.assertEqual(charOccurrences("AhmedAA"), {'A': 3, 'h': 1, 'm': 1, 'e': 1, 'd': 1})

    def testCase2(self):
        self.assertEqual(charOccurrences("mmm ahn 12 a"), {'m': 3, ' ': 3, 'a': 2,
                                                           'h': 1, 'n': 1, '1': 1, '2': 1})
    def testCase3(self):
        self.assertEqual(charOccurrences(" "), {' ': 1})


if __name__ == "__main__":
    unittest.main()
