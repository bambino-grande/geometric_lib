import unittest

def area(a, h): 
    '''
    Возвращает площадь треугольника по длинам его высоты и стороны (a, h)

        Параметры:
            a (float): длина стороны треугольника
            h (float): длина высоты треугольника

        Возвращаемое значение:
            (float): полученная площадь треугольника

    Примеры вызова:
        area(3.0, 4.0)    6.0
        area(6.5, 7.2)    23.4
    '''       
    if not isinstance(a, int) or not isinstance(h, int):
        raise TypeError("Сторона и высота треугольника должны быть целыми числами")
    if a <= 0 or h <= 0:
        raise ValueError("Сторона и высота треугольника должны быть больше 0")
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Возвращает периметр треугольника по длинам его сторон (a, b, c)

        Параметры:
            a (float): длина первой стороны треугольника
            b (float): длина второй стороны треугольника
            c (float): длина третьей стороны треугольника

        Возвращаемое значение:
            (float): периметр треугольника

    Примеры вызова:
        perimeter(3.0, 4.0, 5.0)    12.0
        perimeter(6.5, 7.2, 8.3)    22.0
    '''
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise TypeError("Стороны треугольника должны быть целыми числами")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Стороны треугольника должны быть больше 0")
    return a + b + c 

class TriangleTests(unittest.TestCase):
    # Tests for area function
    def test_area_valid_small(self):
        self.assertAlmostEqual(area(2, 4), 4.0, places=2)

    def test_area_valid_large(self):
        self.assertAlmostEqual(area(999221, 214531), 107181940175.5, places=2)

    def test_area_zero_side(self):
        with self.assertRaises(ValueError):
            area(0, 1)

    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            area(223, -3214234)

    def test_area_non_integer_side(self):
        with self.assertRaises(TypeError):
            area('1', 23)

    def test_area_non_integer_height(self):
        with self.assertRaises(TypeError):
            area(3324, "321")
    
    def test_area_float_inputs(self):
        with self.assertRaises(TypeError):
            area(5.5, 10)

    # Tests for perimeter function
    def test_perimeter_valid_small(self):
        self.assertEqual(perimeter(4, 34, 23), 61)

    def test_perimeter_valid_large(self):
        self.assertEqual(perimeter(234, 23, 4325235), 4325492)

    def test_perimeter_zero_side(self):
        with self.assertRaises(ValueError):
            perimeter(0, 324, 4)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(432, 43, -4234234)

    def test_perimeter_non_integer_side(self):
        with self.assertRaises(TypeError):
            perimeter(234, 4, '5')

    def test_perimeter_non_integer_side2(self):
        with self.assertRaises(TypeError):
            perimeter(65, "2343", 164)
    
    def test_perimeter_float_inputs(self):
        with self.assertRaises(TypeError):
            perimeter(10.0, 20, 30)

    # Additional tests for triangle inequality (optional)
    def test_triangle_inequality_violation(self):
        # Although not implemented in the perimeter function, 
        # it's a logical test to ensure triangle validity
        # This will pass since perimeter doesn't check it
        self.assertEqual(perimeter(1, 2, 3), 6)
        # To enforce triangle inequality, you would need to modify the perimeter function

if __name__ == '__main__':
    unittest.main()
