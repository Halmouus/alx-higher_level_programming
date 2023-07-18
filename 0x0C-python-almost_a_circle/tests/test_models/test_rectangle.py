#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import io


class RectangleTestCase(unittest.TestCase):
    """Test class for Rectangle class"""
    def test_a_positional_arguments(self):
        """Test positional argument validation"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_a_the_ids(self):
        """Test id coherence and duplication
        and the validity of types and values"""
        self.assertEqual(Rectangle(10, 9).id, 1)
        self.assertEqual(Rectangle(10, 9, 0, 0, None).id, 2)
        self.assertEqual(Rectangle(10, 9).id, 3)
        self.assertEqual(Rectangle(10, 9, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 4)
        self.assertEqual(Rectangle(10, 9, 0, 0, 5).id, 5)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 6)
        self.assertEqual(Rectangle(10, 9, 0, 0, 5000).id, 5000)

    def test_b_width(self):
        """Test width value validation"""
        with self.assertRaises(TypeError):
            Rectangle('str', 9, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 9, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(-4, 9, 0, 0)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 7)

    def test_c_height(self):
        """Test height value validation"""
        with self.assertRaises(TypeError):
            Rectangle(5, 'str', 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(5, -5, 0, 0)
        self.assertEqual(Rectangle(10, 9, 0, 0).id, 8)

    def test_d_x(self):
        """Test x value validation"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 'str', 0)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 0)
        self.assertEqual(Rectangle(5, 10, 4, 0).id, 9)

    def test_e_y(self):
        """Test y value validation"""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 0, 'str')
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 0, -1)
        self.assertEqual(Rectangle(5, 10, 0, 4).id, 10)

    def test_f_type(self):
        """Test type of Rectangle"""
        class_type = "<class 'models.rectangle.Rectangle'>"
        self.assertEqual(str(type(Rectangle(10, 5))), class_type)
        self.assertEqual(Rectangle(10, 5).__dict__,
                         {'_Rectangle__width': 10, '_Rectangle__height': 5,
                         '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 13})

    def test_g_type(self):
        "Test type and isinstance"
        self.assertTrue(type(Rectangle(10, 5)) == Rectangle)
        self.assertFalse(type(Rectangle(10, 5)) == Base)
        self.assertTrue(isinstance(Rectangle(10, 5), Rectangle))
        self.assertTrue(isinstance(Rectangle(10, 5), Base))

    def test_h_area(self):
        """Test area public method of Rectangle"""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(10, 5, 0, 0).area(), 50)
        self.assertEqual(Rectangle(100, 50).area(), 5000)
        with self.assertRaises(TypeError):
            Rectangle(10, 5).area(3)

    def test_i_display(self):
        """Test display method of Rectangle"""
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Rectangle(5, 3).display()
            disp = my_stdout.getvalue()
        expected_disp = '#####\n#####\n#####\n'
        self.assertEqual(disp, expected_disp)
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Rectangle(5, 3, 1, 0).display()
            disp = my_stdout.getvalue()
        expected_disp = ' #####\n #####\n #####\n'
        self.assertEqual(disp, expected_disp)
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Rectangle(1, 1, 0, 1).display()
            disp = my_stdout.getvalue()
        expected_disp = '\n#\n'
        self.assertEqual(disp, expected_disp)
        with patch('sys.stdout', new=io.StringIO()) as my_stdout:
            Rectangle(4, 4, 3, 2).display()
            disp = my_stdout.getvalue()
        expected_disp = '\n\n   ####\n   ####\n   ####\n   ####\n'
        self.assertEqual(disp, expected_disp)
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 1, 5).display(3)

    def test_j_set_get_width(self):
        "test width setters and getters"
        rect = Rectangle(4, 2)
        self.assertEqual(rect.width, 4)
        rect.width = 10
        self.assertEqual(rect.width, 10)
        with self.assertRaises(TypeError):
            rect.width = '6'
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_k_set_get_height(self):
        "test height setters and getters"
        rect = Rectangle(4, 2)
        self.assertEqual(rect.height, 2)
        rect.height = 10
        self.assertEqual(rect.height, 10)
        with self.assertRaises(TypeError):
            rect.height = '6'
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_k_set_get_x(self):
        "test x setters and getters"
        rect = Rectangle(4, 2, 0, 0)
        self.assertEqual(rect.x, 0)
        rect.x = 10
        self.assertEqual(rect.x, 10)
        with self.assertRaises(TypeError):
            rect.x = '12'
        with self.assertRaises(ValueError):
            rect.x = -3

    def test_l_set_get_y(self):
        "test y setters and getters"
        rect = Rectangle(4, 2, 0, 0)
        self.assertEqual(rect.y, 0)
        rect.y = 10
        self.assertEqual(rect.y, 10)
        with self.assertRaises(TypeError):
            rect.y = '12'
        with self.assertRaises(ValueError):
            rect.y = -3

    def test_m_str(self):
        "test string representation of Rectangle object"
        r1 = Rectangle(4, 6, 2, 1, 100)
        self.assertEqual(str(r1), "[Rectangle] (100) 2/1 - 4/6")
        r2 = Rectangle(5, 10)
        self.assertEqual(str(r2), "[Rectangle] (32) 0/0 - 5/10")

    def test_n_update_1(self):
        "test update method of Recangle object"
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (33) 10/10 - 10/10")
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (33) 10/10 - 10/10")
        r1.update(666)
        self.assertEqual(str(r1), "[Rectangle] (666) 10/10 - 10/10")
        r1.update(666, 2)
        self.assertEqual(str(r1), "[Rectangle] (666) 10/10 - 2/10")
        r1.update(666, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (666) 10/10 - 2/3")
        r1.update(666, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (666) 4/10 - 2/3")
        r1.update(666, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (666) 4/5 - 2/3")

    def test_n_update_2(self):
        "test special cases for update method of Recangle"
        r2 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r2), "[Rectangle] (34) 10/10 - 10/10")
        with self.assertRaises(TypeError):
            r2.update(667, 'str')
        with self.assertRaises(ValueError):
            r2.update(667, 0)
        with self.assertRaises(ValueError):
            r2.update(667, -5)
        with self.assertRaises(ValueError):
            r2.update(667, 1, 0)
        with self.assertRaises(ValueError):
            r2.update(667, 1, -5)
        with self.assertRaises(TypeError):
            r2.update(667, 1, 'str')
        with self.assertRaises(ValueError):
            r2.update(667, 1, 2, -4)
        with self.assertRaises(ValueError):
            r2.update(667, 1, 2, 3, -5)
        with self.assertRaises(IndexError):
            r2.update(667, 1, 2, 3, 4, 5, 6)

    def test_o_update_1(self):
        "test update method #2 for Rectangle"
        rect = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect), "[Rectangle] (35) 10/10 - 10/10")
        rect.update()
        self.assertEqual(str(rect), "[Rectangle] (35) 10/10 - 10/10")
        rect.update(width=20)
        self.assertEqual(str(rect), "[Rectangle] (35) 10/10 - 20/10")
        rect.update(height=15, width=30)
        self.assertEqual(str(rect), "[Rectangle] (35) 10/10 - 30/15")
        rect.update(y=0, id=256, width=30)
        self.assertEqual(str(rect), "[Rectangle] (256) 10/0 - 30/15")
        rect.update(y=8, id=35, width=36, x=4, height=23)
        self.assertEqual(str(rect), "[Rectangle] (35) 4/8 - 36/23")
        rect.update(500, y=8, id=35, width=36, x=4, height=23)
        self.assertEqual(str(rect), "[Rectangle] (500) 4/8 - 36/23")
        rect.update(550, 256, 128, 10, 20, y=8, id=35, width=36, x=4,
                    height=23)
        self.assertEqual(str(rect), "[Rectangle] (550) 10/20 - 256/128")

    def test_o_update_2(self):
        "test update method #2 for Rectangle"
        rect_o = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rect_o), "[Rectangle] (36) 10/10 - 10/10")
        with self.assertRaises(TypeError):
            rect_o.update(id=35, height='str')
        with self.assertRaises(ValueError):
            rect_o.update(height=0)
        with self.assertRaises(ValueError):
            rect_o.update(height=-5)
        with self.assertRaises(ValueError):
            rect_o.update(width=0)
        with self.assertRaises(ValueError):
            rect_o.update(width=-5)
        with self.assertRaises(TypeError):
            rect_o.update(width='str')
        with self.assertRaises(ValueError):
            rect_o.update(x=-4)
        with self.assertRaises(ValueError):
            rect_o.update(y=-5)

    def test_p_dict_rep(self):
        "test dictionary representation of a Rectangle"
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] (37) 1/9 - 10/2")
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 37,
                                         'height': 2, 'width': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        self.assertEqual(str(r2), "[Rectangle] (38) 0/0 - 1/1")
        r2.update(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (37) 1/9 - 10/2")
        self.assertFalse(r1 == r2)

    def test_q_json(self):
        json_dictionary = Base.to_json_string(None)
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(json_dictionary, "[]")
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        exp_dict = {'x': 2, 'width': 10, 'id': 39, 'height': 7, 'y': 8}
        exp_json = '[{"x": 2, "width": 10, "id": 39, "height": 7, "y": 8}]'
        self.assertEqual(dictionary, exp_dict)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, exp_json)
        self.assertEqual(type(json_dictionary), str)


if __name__ == '__main__':
    unittest.main()