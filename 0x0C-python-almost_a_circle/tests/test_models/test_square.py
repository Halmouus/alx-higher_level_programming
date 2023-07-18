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
        self.assertEqual(Square(10, 0, 0, 5).id, 5)
        self.assertEqual(Square(10, 0, 0).id, 6)
        self.assertEqual(Square(10, 0, 0, 5000).id, 5000)

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
        "test size setters and getters"
        sqr = Square(4)
        self.assertEqual(sqr.size, 4)
        sqr.size = 10
        self.assertEqual(sqr.size, 10)
        with self.assertRaises(TypeError):
            sqr.size = '6'
        with self.assertRaises(ValueError):
            sqr.size = 0

    def test_m_str(self):
        "test string representation of Square object"
        sqr1 = Square(4, 2, 1, 100)
        self.assertEqual(str(sqr1), "[Square] (100) 2/1 - 4")
        sqr2 = Square(10)
        self.assertEqual(str(sqr2), "[Square] (30) 0/0 - 10")

    def test_n_update_1(self):
        "test update method of Recangle object"
        sqr1 = Square(10, 10, 10)
        self.assertEqual(str(sqr1), "[Square] (31) 10/10 - 10")
        sqr1.update()
        self.assertEqual(str(sqr1), "[Square] (31) 10/10 - 10")
        sqr1.update(666)
        self.assertEqual(str(sqr1), "[Square] (666) 10/10 - 10")
        sqr1.update(666, 2)
        self.assertEqual(str(sqr1), "[Square] (666) 10/10 - 2")
        sqr1.update(666, 2, 4)
        self.assertEqual(str(sqr1), "[Square] (666) 4/10 - 2")
        sqr1.update(666, 2, 4, 5)
        self.assertEqual(str(sqr1), "[Square] (666) 4/5 - 2")

    def test_n_update_2(self):
        "test special cases for update method of Recangle"
        sqr2 = Square(10, 10, 10)
        self.assertEqual(str(sqr2), "[Square] (32) 10/10 - 10")
        with self.assertRaises(TypeError):
            sqr2.update(667, 'str')
        with self.assertRaises(ValueError):
            sqr2.update(667, 0)
        with self.assertRaises(ValueError):
            sqr2.update(667, -5)
        with self.assertRaises(ValueError):
            sqr2.update(667, 0)
        with self.assertRaises(ValueError):
            sqr2.update(667, -5)
        with self.assertRaises(TypeError):
            sqr2.update(667, 'str')
        with self.assertRaises(ValueError):
            sqr2.update(667, 2, -4)
        with self.assertRaises(ValueError):
            sqr2.update(667, 2, 3, -5)
        with self.assertRaises(IndexError):
            sqr2.update(667, 2, 3, 5, 6)

    def test_o_update_1(self):
        "test update method #2 for Square"
        sqr = Square(10, 10, 10)
        self.assertEqual(str(sqr), "[Square] (33) 10/10 - 10")
        sqr.update()
        self.assertEqual(str(sqr), "[Square] (33) 10/10 - 10")
        sqr.update(size=20)
        self.assertEqual(str(sqr), "[Square] (33) 10/10 - 20")
        sqr.update(size=30)
        self.assertEqual(str(sqr), "[Square] (33) 10/10 - 30")
        sqr.update(y=0, id=256, size=30)
        self.assertEqual(str(sqr), "[Square] (256) 10/0 - 30")
        sqr.update(y=8, id=33, size=36, x=4)
        self.assertEqual(str(sqr), "[Square] (33) 4/8 - 36")
        sqr.update(500, y=8, id=33, size=36, x=4)
        self.assertEqual(str(sqr), "[Square] (500) 4/8 - 36")
        sqr.update(550, 256, 10, 20, y=8, id=33, size=36, x=4)
        self.assertEqual(str(sqr), "[Square] (550) 10/20 - 256")

    def test_o_update_2(self):
        "test update method #2 for Square"
        sqr_o = Square(10, 10, 10)
        self.assertEqual(str(sqr_o), "[Square] (34) 10/10 - 10")
        with self.assertRaises(TypeError):
            sqr_o.update(id=33, size='str')
        with self.assertRaises(ValueError):
            sqr_o.update(size=0)
        with self.assertRaises(ValueError):
            sqr_o.update(size=-5)
        with self.assertRaises(ValueError):
            sqr_o.update(x=-4)
        with self.assertRaises(ValueError):
            sqr_o.update(y=-5)

    def test_p_dict_rep(self):
        "test dictionary representation of a Square"
        s1 = Square(10, 1, 9)
        self.assertEqual(str(s1), "[Square] (35) 1/9 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'x': 1, 'y': 9, 'id': 35,
                                         'size': 10})
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1)
        self.assertEqual(str(s2), "[Square] (36) 0/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (35) 1/9 - 10")
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()