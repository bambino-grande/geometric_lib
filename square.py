import unittest

def area(a):
    '''
    Возвращает площадь квадрата по длине его стороны (a)

        Параметры:
            a (int): длина стороны квадрата

        Возвращаемое значение:
            (int): площадь квадрата

    Примеры вызова:
        area(4)     16
        area(2)     4
    '''
    if not isinstance(a, int):
        raise TypeError("Сторона квадрата должна быть целым числом")
    if a <= 0:
        raise ValueError("Сторона квадрата должна быть больше 0")
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата по длине его стороны (a)

        Параметры:
            a (int): длина стороны квадрата

        Возвращаемое значение:
            (int): периметр квадрата

    Примеры вызова:
        perimeter(4)    16
        perimeter(2)    8
    '''
    if not isinstance(a, int):
        raise TypeError("Сторона квадрата должна быть целым числом")
    if a <= 0:
        raise ValueError("Сторона квадрата должна быть больше 0")
    return 4 * a


class SquareTests(unittest.TestCase):
    # Tests for area function
    def test_area_valid_small(self):
        self.assertEqual(area(4), 16)

    def test_area_valid_large(self):
        self.assertEqual(area(6342645421), 40229150936532267241)

    def test_area_zero_side(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-56235552)

    def test_area_non_integer_input(self):
        with self.assertRaises(TypeError):
            area('4')

    def test_area_non_integer_input_2(self):
        with self.assertRaises(TypeError):
            area("5423529")

    def test_area_float_input(self):
        with self.assertRaises(TypeError):
            area(2.5)

    # Tests for perimeter function
    def test_perimeter_valid_small(self):
        self.assertEqual(perimeter(72), 288)

    def test_perimeter_valid_large(self):
        self.assertEqual(perimeter(6346723), 25386892)

    def test_perimeter_zero_side(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-7542546)

    def test_perimeter_non_integer_input(self):
        with self.assertRaises(TypeError):
            perimeter('52384')

    def test_perimeter_non_integer_input_2(self):
        with self.assertRaises(TypeError):
            perimeter("72313==3?sg33473")

    def test_perimeter_float_input(self):
        with self.assertRaises(TypeError):
            perimeter(2.5)


if __name__ == '__main__':
    unittest.main()
