import math
import unittest

def area(r):
    '''
    Возвращает площадь круга по длине его радиуса (r)
        
        Параметры:
            r (float или int): длина радиуса круга

        Возвращаемое значение:
            (float): площадь круга

    Примеры вызова:
        area(3)     28.274333882308138
        area(1)     3.141592653589793
        area(2.5)   19.634954084936208
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус круга должен быть числом")
    if r <= 0:
        raise ValueError("Радиус круга должен быть больше 0")
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности по длине его радиуса (r)
        
        Параметры:
            r (float или int): радиус круга

        Возвращаемое значение:
            (float): длина окружности

    Примеры вызова:
        perimeter(3)    18.84955592153876
        perimeter(1)    6.283185307179586
        perimeter(2.5)  15.707963267948966
    '''
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус круга должен быть числом")
    if r <= 0:
        raise ValueError("Радиус круга должен быть больше 0")
    return 2 * math.pi * r


class CircleTests(unittest.TestCase):
    # Tests for area function
    def test_area_valid_integer_small(self):
        self.assertAlmostEqual(area(2), 12.566, places=3)

    def test_area_valid_integer_large(self):
        self.assertAlmostEqual(area(999222), 3.141592653589793 * 999222 ** 2, places=2)

    def test_area_valid_float_small(self):
        self.assertAlmostEqual(area(2.5), 19.634954084936208, places=5)

    def test_area_valid_float_large(self):
        self.assertAlmostEqual(area(1e6), math.pi * 1e12, places=2)

    def test_area_zero_radius(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-3214234)

    def test_area_non_numeric_string(self):
        with self.assertRaises(TypeError):
            area('1')

    def test_area_non_numeric_string_complex(self):
        with self.assertRaises(TypeError):
            area("321abc")

    def test_area_non_numeric_none(self):
        with self.assertRaises(TypeError):
            area(None)

    def test_area_non_numeric_list(self):
        with self.assertRaises(TypeError):
            area([5])

    # Tests for perimeter function
    def test_perimeter_valid_integer_small(self):
        self.assertAlmostEqual(perimeter(4), 25.133, places=3)

    def test_perimeter_valid_integer_large(self):
        self.assertAlmostEqual(perimeter(345346), 2 * math.pi * 345346, places=2)

    def test_perimeter_valid_float_small(self):
        self.assertAlmostEqual(perimeter(2.5), 15.707963267948966, places=5)

    def test_perimeter_valid_float_large(self):
        self.assertAlmostEqual(perimeter(1e6), 2 * math.pi * 1e6, places=2)

    def test_perimeter_zero_radius(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            perimeter(-4234234)

    def test_perimeter_non_numeric_string(self):
        with self.assertRaises(TypeError):
            perimeter('5')

    def test_perimeter_non_numeric_string_complex(self):
        with self.assertRaises(TypeError):
            perimeter("2343xyz")

    def test_perimeter_non_numeric_none(self):
        with self.assertRaises(TypeError):
            perimeter(None)

    def test_perimeter_non_numeric_list(self):
        with self.assertRaises(TypeError):
            perimeter([10])

    def test_perimeter_float_input(self):
        self.assertAlmostEqual(perimeter(3.1415), 2 * math.pi * 3.1415, places=4)


if __name__ == '__main__':
    unittest.main()
