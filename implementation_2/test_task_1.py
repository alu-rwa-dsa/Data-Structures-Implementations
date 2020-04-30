import unittest
from implementation_2.task_1 import delete_whitespaces


class Test(unittest.TestCase):
    """
    Test class tests different possible string inputs to deleteWhitespaces against there expected output
    if the function output matches the expected given output; return Ok
    """

    def testCase1(self):
        self.assertEqual(delete_whitespaces("hello       my        friend"), "hello my friend")

    def testCase2(self):
        self.assertEqual(delete_whitespaces("   e  my   123    friend"), "e my 123 friend")

    def testCase3(self):
        self.assertEqual(delete_whitespaces("                "), "")


if __name__ == "__main__":
    unittest.main()
