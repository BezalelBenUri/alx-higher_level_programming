#!/usr/bin/python3
import unittest
from models.square import Square
import sys
from io import StringIO
import pep8
from models.base import Base
import json
from models.rectangle import Rectangle
import os
"""
This module contains all unittest for Base class
"""


class TestBase(unittest.TestCase):
    """
    Class of functions to run tests
    """
    def setUp(self):
        """
        function to redirect stdout
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        Tests for pep8 model
        """
        
        pi8= pep8.StyleGuide(quiet=True)
        p = pi8.check_files(['models/base.py'])
        self.aissertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8 test
        """
        pi8 = pep8.StyleGuide(quiet=True)
        p = pi8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstrings(self):
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Base.__doc__)
        self.assertIs(hasattr(Base, "__init__"), True)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIs(hasattr(Base, "create"), True)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIs(hasattr(Base, "to_json_string"), True)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIs(hasattr(Base, "from_json_string"), True)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIs(hasattr(Base, "save_to_file"), True)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIs(hasattr(Base, "load_from_file"), True)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_id(self):
        """
        Test check for id 
        """
        Base._Base__nb_objects = 0
        ba = Base()
        bb = Base()
        bc = Base()
        bd = Base(12)
        be = Base()
        self.assertEqual(ba.id, 1)
        self.assertEqual(bb.id, 2)
        self.assertEqual(bc.id, 3)
        self.assertEqual(bd.id, 12)
        self.assertEqual(be.id, 4)

    def test_from_json_string(self):
        """
        Test check from json string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {'x': 2, 'width': 10,
                                       'id': 1, 'height': 7,
                                       'y': 8})
            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 10, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                               '"y": 8}]'))

    def test_rectangle(self):
        """
        Test check for rectangle
        """
        Ra = Rectangle(4, 5, 6)
        Ra_dict = Ra.to_dictionary()
        Rb = Rectangle.create(**Ra_dict)
        self.assertNotEqual(Ra, Rb)

    def test_square(self):
        """
        Test check for square creation
        """
        Sa = Square(44, 55, 66, 77)
        Sa_dict = Sa.to_dictionary()
        Sa = Rectangle.create(**Sa_dict)
        self.assertNotEqual(Sa, Sb)

    def test_file_rectangle(self):
        """
        Test check if file loads from rectangle
        """
        Ra = Rectangle(33, 34, 35, 26)
        Rb = Rectangle(202, 2)
        lR = [Ra, Rb]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_file_square(self):
        """
        Test check if file loads from square
        """
        Sa = Square(22)
        Sb = Square(44, 44, 55, 66)
        lS = [Sa, Sb]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)
