#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io


class SquareTestCase(unittest.TestCase):
    """Test class for Square class"""
    def test_a_positional_arguments(self):
        """Test positional argument validation"""
        with self.assertRaises(TypeError):
            Square()

    def test_a_the_ids(self):
        """Test id coherence and duplication
        and the validity of types and values"""
        self.assertEqual(Square(10).id, 1)
        self.assertEqual(Square(10, 0, 0, None).id, 2)
        self.assertEqual(Square(10).id, 3)
        self.assertEqual(Square(10, 0, 0, 12).id, 12)
        self.assertEqual(Square(10, 0, 0).id, 4)
        with self.assertRaises(ValueError):
            Square(10, 0, 0, 3)
        with self.assertRaises(ValueError):
            Square(10, 0, 0, 1)
        with self.assertRaises(ValueError):
            Square(10, 0, 0, 12)
        self.assertEqual(Square(10, 0, 0, 5).id, 5)
        self.assertEqual(Square(10, 0, 0).id, 6)
        with self.assertRaises(ValueError):
            Square(10, 0, 0, 6)
        self.assertEqual(Square(10, 0, 0, 5000).id, 5000)
        with self.assertRaises(ValueError):
            Square(10, 0, 0, 3)
        with self.assertRaises(ValueError):
            Square(10, 0, 0, 5000)

    def test_b_size(self):
        """Test size value validation"""
        with self.assertRaises(TypeError):
            Square('str', 0, 0)
        with self.assertRaises(ValueError):
            Square(0, 0, 0)
        with self.assertRaises(ValueError):
            Square(-4, 0, 0)
        self.assertEqual(Square(10, 0, 0).id, 7)

    def test_d_x(self):
        """Test x value validation"""
        with self.assertRaises(TypeError):
            Square(10, 'str', 0)
        with self.assertRaises(ValueError):
            Square(10, -1, 0)
        self.assertEqual(Square(10, 4, 0).id, 8)

    def test_e_y(self):
        """Test y value validation"""
        with self.assertRaises(TypeError):
            Square(10, 0, 'str')
        with self.assertRaises(ValueError):
            Square(10, 0, -1)
        self.assertEqual(Square(10, 0, 4).id, 9)

    def test_f_type(self):
        """Test type of Square"""
        class_type = "<class 'models.square.Square'>"
        self.assertEqual(str(type(Square(10, 5))), class_type)
        self.assertEqual(Square(10).__dict__,
                         {'_Rectangle__width': 10, '_Rectangle__height': 10,
                         '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 11})

    def test_g_type(self):
        "Test type and isinstance"
        self.assertTrue(type(Square(10)) == Square)
        self.assertFalse(type(Square(10)) == Rectangle)
        self.assertFalse(type(Square(10)) == Base)
        self.assertTrue(isinstance(Square(10), Square))
        self.assertTrue(isinstance(Square(10), Rectangle))
        self.assertTrue(isinstance(Square(10), Base))

    def test_h_area(self):
        """Test area public method of Square"""
        self.assertEqual(Square(3).area(), 9)
        self.assertEqual(Square(2).area(), 4)
        self.assertEqual(Square(10, 0, 0).area(), 100)
        self.assertEqual(Square(100).area(), 10000)
        with self.assertRaises(TypeError):
            Square(10).area(3)

    def test_i_display(self):
        """Test display method of Square"""
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Square(3).display()
            disp = my_stdout.getvalue()
        expected_disp = '###\n###\n###\n'
        self.assertEqual(disp, expected_disp)
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Square(3, 1, 0).display()
            disp = my_stdout.getvalue()
        expected_disp = ' ###\n ###\n ###\n'
        self.assertEqual(disp, expected_disp)
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Square(1, 0, 1).display()
            disp = my_stdout.getvalue()
        expected_disp = '\n#\n'
        self.assertEqual(disp, expected_disp)
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Square(4, 3, 2).display()
            disp = my_stdout.getvalue()
        expected_disp = '\n\n   ####\n   ####\n   ####\n   ####\n'
        self.assertEqual(disp, expected_disp)
        with self.assertRaises(TypeError):
            Square(10, 1, 5).display(3)

    def test_k_set_get_size(self):
        "test height setters and getters"
        sqr = Square(4)
        self.assertEqual(sqr.size, 4)
        sqr.size = 10
        self.assertEqual(sqr.size, 10)
        with self.assertRaises(TypeError):
            sqr.size = '6'
        with self.assertRaises(ValueError):
            sqr.size = 0

if __name__ == '__main__':
    unittest.main()