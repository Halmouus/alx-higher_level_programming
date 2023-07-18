#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
from models.base import Base


class BaseTestCase(unittest.TestCase):
    """Test class for Base class"""
    def test_a_id(self):
        """Test id coherence"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(None).id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 4)

    def test_c_special_values(self):
        """Test for special values output"""
        self.assertEqual(Base().id, 5)
        self.assertEqual(Base(0).id, 0)
        with self.assertRaises(ValueError):
            Base(-1)
        self.assertEqual(Base().id, 6)

    def test_d_special_values_2(self):
        """Test for special values output"""
        self.assertEqual(Base().id, 7)
        with self.assertRaises(TypeError):
            Base("str")
        self.assertEqual(Base().id, 8)

    def test_e_class_type(self):
        """Test for type and dictionary representation"""
        self.assertEqual(str(type(Base())), "<class 'models.base.Base'>")
        self.assertEqual(Base().__dict__, {'id': 10})

    def test_f_special_values(self):
        """Test for special values output : lists and tuples"""
        with self.assertRaises(TypeError):
            Base([10, 20, 30])
        with self.assertRaises(TypeError):
            Base(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            Base(('a', 1, 'str', 0, [0, 1, 2]))

    def test_g_private_attribute_access(self):
        """Test for type and dictionary representation"""
        with self.assertRaises(AttributeError):
            Base().__nb_objects
        with self.assertRaises(AttributeError):
            Base().__id_list

    def test_h_json(self):
        "Test json conversion method"
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(Base.to_json_string([dictionary]), json_string)


if __name__ == '__main__':
    unittest.main()