#!/usr/bin/python3
"""tests for the User class"""
from models import state as st
import unittest


class TestInstance(unittest.TestCase):

    def test_instance_is_alive(self):
        """test_instance_is_alive
            check if the instence is a user instance
        """

        instance = st.State()
        self.assertIsInstance(instance, st.State)
        
class TestInstancesEquality(unittest.TestCase):

    def test_not_the_same_id(self):
        """not_the_same_id
            two instances of the base_model must not have the same id
        """
        instance1 = st.State()
        instance2 = st.State()
        self.assertNotEqual(instance1.id, instance2.id)
    
    def test_the_kwargs_setup(self):
        """test_the_kwargs_setup
            testing if the kwargs set up works fine
        """
        ob1 = st.State()# create a User instance
        # set up the rest of attributes
        
        ob_dict = ob1.to_dict()# getting the dict
        # passing the dict to create an instance
        ob2 = st.State(**ob_dict)
        
        # the two instances must not be the same 
        # but they should have the same dict
        self.assertNotEqual(ob1, ob2)
        # checking if the two dicts are equal
        self.assertEqual(ob_dict, ob2.to_dict())

if __name__ == '__main__':
    unittest.main()