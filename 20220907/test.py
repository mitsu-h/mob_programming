"""
TODO
- [*] "20 5 /"を入力する -> 4を返す
- [*] "4 2 +"を入力 -> 6を返す
- [] "4 2 + 3 -"を入力 -> 3を返す
- [] "3 5 8 * 7 + *"を入力 -> 141を返す
- [] "9 SQRT"を入力 -> 3を返す
- [] "4 5 MAX 1 +"を入力 -> 6を返す
- [] "5 3 4 2 9 1 MAX"を入力 -> Errorを返す
"""
import unittest
from kata import rpn_calc

class TestRPNCalc(unittest.TestCase):
    """
    逆ポーランド記法の計算結果のテスト
    """

    
    def test_divide(self):
        self.assertEqual(rpn_calc("20 5 /"), 4)

    def test_sum(self):
        self.assertEqual(rpn_calc("4 2 +"), 6)
        
    # def test_divide(self):
    #     self.assertEqual(rpn_calc("20 5 /"), 4)

    # def test_sum(self):
    #     self.assertEqual(rpn_calc("4 2 +"), 6)
    """
    def test_access(self):
        
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
    """

if __name__ == "__main__":
    unittest.main()