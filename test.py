from circle import CircleTests
from triangle import TriangleTests
from rectangle import RectangleTests
from square import SquareTests
import unittest


def suite():
    suite_circle = unittest.TestLoader().loadTestsFromTestCase(CircleTests)
    suite_triangle = unittest.TestLoader().loadTestsFromTestCase(TriangleTests)
    suite_rectangle = unittest.TestLoader().loadTestsFromTestCase(RectangleTests)
    suite_square = unittest.TestLoader().loadTestsFromTestCase(SquareTests)

    return unittest.TestSuite([suite_circle, suite_triangle, suite_rectangle, suite_square])


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())