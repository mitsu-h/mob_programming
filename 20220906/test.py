import unittest
from kata import manhattan_distance, Point

class TestManhattan(unittest.TestCase):
    """
    FizzBuzzのテスト
    """

    def test_access(self):
        """Pointインスタンスのメンバにアクセスする
        期待する結果は例外送出をする
        """
        point = Point(1, 1)
        with self.assertRaises(AttributeError) as e:
            point.x
        with self.assertRaises(AttributeError) as e:
            point.y

    def test_diff_same(self):
        point = Point(1, 1)
        self.assertEqual(point.diff_point(Point(1, 1)),(0, 0))

    def test_diff_posi(self):
        point = Point(5, 4)
        self.assertEqual(point.diff_point(Point(3, 2)),(2, 2))

    def test_diff_nega(self):
        point = Point(1, 1)
        self.assertEqual(point.diff_point(Point(0, 3)),(1, -2))

    def test_manhattan_same(self):
        self.assertEqual(manhattan_distance(Point(1, 1), Point(1, 1)), 0)

    def test_manhattan_posi(self):
        self.assertEqual(manhattan_distance(Point(5, 4), Point(3, 2)), 4)

    def test_manhattan_nega(self):
        self.assertEqual(manhattan_distance(Point(1, 1), Point(0, 3)), 3)


if __name__ == "__main__":
    unittest.main()