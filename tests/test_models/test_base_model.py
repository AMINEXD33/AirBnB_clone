#!/usr/bin/python3
"""tests for the BaseModule"""
from string import ascii_letters as ASCII
import random
import unittest
from models import base_model as bm

class TestInstance(unittest.TestCase):

    def test_instance_is_alive(self):
        """test_instance_is_alive
            check if the instence is indeed a BaseModel instance
        """

        instance = bm.BaseModel()
        self.assertIsInstance(instance, bm.BaseModel)

class TestInstancesEquality(unittest.TestCase):

    def test_not_the_same_id(self):
        """not_the_same_id
            two instances of the base_model must not have the same id
        """
        instance1 = bm.BaseModel()
        instance2 = bm.BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

class TestInitializingWithDict(unittest.TestCase):

    def test_not_the_same_but_the_same_content(self):
        """test_not_the_same_but_the_same_content
            play around with initializer
        """
        # get the dict from the instance
        instance1 = bm.BaseModel()
        instance1_dict = instance1.to_dict()
        # initialize the new instance with the dict
        instance2 = bm.BaseModel(**instance1_dict)

        # the instances are not equal (DUH!)
        self.assertNotEqual(instance1, instance2)

        # the instances have the same dict
        self.assertEqual(instance1.to_dict(), instance2.to_dict())

    def test_currupted_overloaded_dict(self):
        """test_currupted_dict
            passing a dict containing a lot of other keys and values
            but note that the attributes required are availble

            EXPECTATION: we're expecting the __init__ of the BaseModel to
                  only pick the correct attributes from the overloaded
                  dict
        """
        # get the dict from the instance
        instance1 = bm.BaseModel()
        instance1_dict = instance1.to_dict()
        # let's overloade it
        for x in range(100):
            key, value = "", ""
            for y in range(10):
                key += random.choice(ASCII)
                value += random.choice(ASCII)
            instance1_dict[key] = value

        # lets try to initialize the instance with the new overloaded dict
        instance2 = bm.BaseModel(**instance1_dict)
        # ok now let't run this previous test
        self.test_not_the_same_but_the_same_content()

    def test_currupted_underloade_dict(self):
        """test_currupted_underloade_dict
        passing a dict that is underloaded, meaning it doesn't contain
        all the attributes needed

        EXPECTATION: we're expecting from the __init__ once it detects that
                    the dict is not completed to initialize the object using
                    the standard logic (plz see the models/base_model.py)
        """
        # get the dict from the instance
        instance1 = bm.BaseModel()
        instance1_dict = instance1.to_dict()

        #underloaded dict
        variant= {"as":"asdad", "asd":[123,"12424",None]}

        # let's initialize the new object using this underloaded dict
        instance2 = bm.BaseModel(variant)
        # let's check if it initialized
        self.assertIsInstance(instance2, bm.BaseModel)

        # the two instances have the same dict lenght
        self.assertEqual(len(instance1_dict), len(instance2.to_dict()))

    def test_pass_an_empy_as_dict(self):
        """test_pass_null_as_dict
            we're passing an empty as a dict to initialize the object

            EXPECTATION: we're expecting from the __init__ to just
                        ignore the empty dict and initialize the object
                        using the standard logic (plz see the models/base_model.py)
        """
        instance2 = bm.BaseModel(**{})
        # let's check if it initialized
        self.assertIsInstance(instance2, bm.BaseModel)
    

if __name__ == '__main__':
    unittest.main()

