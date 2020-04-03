import unittest  # import the unittest module to test the class methods

from implementation_6.Fibonacci import fibonacci


class TestFib(unittest.TestCase):
    def test1(self):
        self.assertEqual(fibonacci(0), 0)

    def test2(self):
        self.assertEqual(fibonacci(2), 1)

    def test3(self):
        self.assertEqual(fibonacci(5), 5)

    def test4(self):
        self.assertEqual(fibonacci(20), 6765)


if __name__ == '__main__':
    unittest.main()
