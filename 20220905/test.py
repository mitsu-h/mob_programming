import unittest
from kata import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    """
    FizzBuzzのテスト
    """

    def test_input_1(self):
        self.assertEqual(fizzbuzz(1), "1")

    def test_input_2(self):
        self.assertEqual(fizzbuzz(2), "2")

    def test_input_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_input_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_input_6(self):
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_input_10(self):
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_input_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_input_30(self):
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()