import unittest

def area(a, b): 
    '''
    Возвращает площадь прямоугольника.

        Входные данные:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника
            
        Выходные данные:
            area (int): площадь прямоугольника
            
        Пример вызова:
            area(5, 10) - вернёт 50
    '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Стороны прямоугольника должны быть целыми числами")
    if a <= 0 or b <= 0:
        raise ValueError("Стороны прямоугольника должны быть больше 0")
    return a * b 

def perimeter(a, b): 
    '''
    Возвращает периметр прямоугольника.

        Входные данные:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника
            
        Выходные данные:
            perimeter (int): периметр прямоугольника
            
        Пример вызова:
            perimeter(5, 10) - вернёт 30
    '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Стороны прямоугольника должны быть целыми числами")
    if a <= 0 or b <= 0:
        raise ValueError("Стороны прямоугольника должны быть больше 0")
    return 2 * (a + b)

class RectangleTests(unittest.TestCase):
    # Tests for area function
    def test_area_valid_small(self):
        self.assertEqual(area(2, 4), 8)

    def test_area_valid_large(self):
        self.assertEqual(area(999221, 214531), 999221 * 214531)
    
    def test_area_zero_side_a(self):
        with self.assertRaises(ValueError):
            area(0, 134)

    def test_area_zero_side_b(self):
        with self.assertRaises(ValueError):
            area(61, -634764)
    
    def test_area_negative_side_a(self):
        with self.assertRaises(ValueError):
            area(-5, 10)
    
    def test_area_negative_side_b(self):
        with self.assertRaises(ValueError):
            area(5, -10)
    
    def test_area_non_integer_a(self):
        with self.assertRaises(TypeError):
            area('4', 8395142)
    
    def test_area_non_integer_b(self):
        with self.assertRaises(TypeError):
            area(897653, "982662945645")
    
    def test_area_both_non_integer(self):
        with self.assertRaises(TypeError):
            area("5", "10")
    
    def test_area_float_inputs_a(self):
        with self.assertRaises(TypeError):
            area(5.5, 10)
    
    def test_area_float_inputs_b(self):
        with self.assertRaises(TypeError):
            area(5, 10.5)
    
    def test_area_non_numeric_none(self):
        with self.assertRaises(TypeError):
            area(None, 10)
    
    def test_area_non_numeric_list(self):
        with self.assertRaises(TypeError):
            area([5], 10)
    
    # Tests for perimeter function
    def test_perimeter_valid_small(self):
        self.assertEqual(perimeter(34, 23), 2 * (34 + 23))  # 114

    def test_perimeter_valid_large(self):
        self.assertEqual(perimeter(23, 4325235), 2 * (23 + 4325235))  # 8650516
    
    def test_perimeter_zero_side_a(self):
        with self.assertRaises(ValueError):
            perimeter(4357, 0)
    
    def test_perimeter_zero_side_b(self):
        with self.assertRaises(ValueError):
            perimeter(432, -4234234)
    
    def test_perimeter_negative_side_a(self):
        with self.assertRaises(ValueError):
            perimeter(-10, 20)
    
    def test_perimeter_negative_side_b(self):
        with self.assertRaises(ValueError):
            perimeter(10, -20)
    
    def test_perimeter_non_integer_a(self):
        with self.assertRaises(TypeError):
            perimeter(234, '36')
    
    def test_perimeter_non_integer_b(self):
        with self.assertRaises(TypeError):
            perimeter("235743", 164)
    
    def test_perimeter_both_non_integer(self):
        with self.assertRaises(TypeError):
            perimeter("235743", "164")
    
    def test_perimeter_float_inputs_a(self):
        with self.assertRaises(TypeError):
            perimeter(34.5, 23)
    
    def test_perimeter_float_inputs_b(self):
        with self.assertRaises(TypeError):
            perimeter(34, 23.5)
    
    def test_perimeter_non_numeric_none(self):
        with self.assertRaises(TypeError):
            perimeter(None, 23)
    
    def test_perimeter_non_numeric_list(self):
        with self.assertRaises(TypeError):
            perimeter([34], 23)

if __name__ == '__main__':
    unittest.main()
