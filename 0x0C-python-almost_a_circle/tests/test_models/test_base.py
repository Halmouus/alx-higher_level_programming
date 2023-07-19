#!/usr/bin/python3
"""Unittest for Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

def read_file(filename):
    with open(filename, "r") as f:
        str = f.read()
    return str

def json_clear():
    json_file = [file for file in os.listdir(os.getcwd())
                  if file.endswith(".json")]
    for file in json_file:
        file_path = os.path.join(os.getcwd(), file)
        os.remove(file_path)

class BaseTestCase(unittest.TestCase):
    """Test class for Base class"""
    @classmethod
    def setUpClass(cls):
        """clears the id queue for the upcoming tests"""
        Base.id_reset()

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

    def test_h_toto_json(self):
        """Test json conversion method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(Base.to_json_string([dictionary]), json_string)

    def test_i_from_json_string(self):
        """Test from_json_string method of Base class"""
        list_input = [{'id': 890, 'width': 10, 'height': 4},
                      {'id': 7010, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        list_format = [{'height': 4, 'width': 10, 'id': 890},
                       {'height': 7, 'width': 1, 'id': 7010}]
        json_format = ('[{"id": 890, "width": 10, "height": 4}, '
                       '{"id": 7010, "width": 1, "height": 7}]')
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(json_list_input, json_format)
        self.assertEqual(list_output, list_format)

    def test_j_to_file(self):
        """test save_to and load_from methods of Base"""
        Base.id_reset()
        json_clear()
        output = ""
        self.assertEqual(Rectangle.str_list(), [])
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        output = read_file("Rectangle.json")
        self.assertEqual(output, "[]")
        Rectangle.save_to_file([])
        output = read_file("Rectangle.json")
        self.assertEqual(output, "[]")
        self.assertEqual(Rectangle.str_list(), [])
        Rectangle.save_to_file([Rectangle(3, 4), Rectangle(5, 8, 1), Rectangle(9, 1, 3, 2)])
        output = read_file("Rectangle.json")
        self.assertEqual(output, '[{"x": 0, "width": 3, "id": 1, "height": 4, "y": 0}, {"x": 1, "width": 5, "id": 2, "height": 8, "y": 0}, {"x": 3, "width": 9, "id": 3, "height": 1, "y": 2}]')
        self.assertEqual(Rectangle.str_list(), ['[Rectangle] (1) 0/0 - 3/4', '[Rectangle] (2) 1/0 - 5/8', '[Rectangle] (3) 3/2 - 9/1'])
        Rectangle.save_to_file([Rectangle(3, 4), Rectangle(5, 8, 1), Rectangle(9, 1, 3, 2)])
        output = read_file("Rectangle.json")
        self.assertEqual(output, '[{"x": 0, "width": 3, "id": 4, "height": 4, "y": 0}, {"x": 1, "width": 5, "id": 5, "height": 8, "y": 0}, {"x": 3, "width": 9, "id": 6, "height": 1, "y": 2}]')
        self.assertEqual(Rectangle.str_list(), ['[Rectangle] (4) 0/0 - 3/4', '[Rectangle] (5) 1/0 - 5/8', '[Rectangle] (6) 3/2 - 9/1'])
        self.assertEqual(Square.str_list(), [])
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        output = read_file("Square.json")
        self.assertEqual(output, '[]')
        self.assertEqual(Square.str_list(), [])
        Square.save_to_file([])
        output = read_file("Square.json")
        self.assertEqual(output, '[]')
        self.assertEqual(Square.str_list(), [])
        Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])
        output = read_file("Square.json")
        self.assertEqual(output, '[{"id": 7, "x": 0, "size": 2, "y": 0}, {"id": 8, "x": 1, "size": 4, "y": 0}, {"id": 9, "x": 3, "size": 7, "y": 4}]')
        self.assertEqual(Square.str_list(), ['[Square] (7) 0/0 - 2', '[Square] (8) 1/0 - 4', '[Square] (9) 3/4 - 7'])
        Square.save_to_file([Square(2), Square(4, 1), Square(7, 3, 4)])
        output = read_file("Square.json")
        self.assertEqual(output, '[{"id": 10, "x": 0, "size": 2, "y": 0}, {"id": 11, "x": 1, "size": 4, "y": 0}, {"id": 12, "x": 3, "size": 7, "y": 4}]')
        self.assertEqual(Square.str_list(), ['[Square] (10) 0/0 - 2', '[Square] (11) 1/0 - 4', '[Square] (12) 3/4 - 7'])

    def test_k_create(self):
        """test create method of Base class"""
        Base.id_reset()
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        self.assertTrue(isinstance(r2, Rectangle))
        shape = Rectangle.create(**{ 'width': 2, 'height': 3 })
        self.assertEqual(str(shape), "[Rectangle] (2) 0/0 - 2/3")
        shape = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12 })
        self.assertEqual(str(shape), "[Rectangle] (3) 12/0 - 2/3")
        shape = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1 })
        self.assertEqual(str(shape), "[Rectangle] (4) 12/1 - 2/3")
        shape = Rectangle.create(**{ 'width': 2, 'height': 3, 'x': 12, 'y': 1, 'id': 89 })
        self.assertEqual(str(shape), "[Rectangle] (89) 12/1 - 2/3")
        shape = Square.create(**{ 'size': 2 })
        self.assertEqual(str(shape), "[Square] (5) 0/0 - 2")
        shape = Square.create(**{ 'size': 2, 'x': 1 })
        self.assertEqual(str(shape), "[Square] (6) 1/0 - 2")
        shape = Square.create(**{ 'size': 2, 'x': 1, 'y': 3 })
        self.assertEqual(str(shape), "[Square] (7) 1/3 - 2")
        shape = Square.create(**{ 'size': 2, 'x': 1, 'y': 3, 'id': 89 })
        self.assertEqual(str(shape), "[Square] (89) 1/3 - 2")


if __name__ == '__main__':
    unittest.main()