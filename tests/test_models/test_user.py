#!/usr/bin/python3
"""tests for the User class"""
from models import user as us
import unittest



class TestInstance(unittest.TestCase):
    
    def test_instance_is_alive(self):
        """test_instance_is_alive
            check if the instence is a user instance
        """
        
        instance = us.User()
        self.assertIsInstance(instance, us.User)
        
class TestInstancesEquality(unittest.TestCase):

    def test_not_the_same_id(self):
        """not_the_same_id
            two instances of the base_model must not have the same id
        """
        instance1 = us.User()
        instance2 = us.User()
        self.assertNotEqual(instance1.id, instance2.id)
    
    def test_the_kwargs_setup(self):
        """test_the_kwargs_setup
            testing if the kwargs set up works fine
        """
        ob1 = us.User()# create a User instance
        # set up the rest of attributes
        ob1.email = "test1231"
        ob1.password = "asdasdasd123"
        ob1.last_name = "amine"
        ob1.first_name = "meftah"
        ob_dict = ob1.to_dict()# getting the dict
        # passing the dict to create an instance
        ob2 = us.User(**ob_dict)
        
        # the two instances must not be the same 
        # but they should have the same dict
        self.assertNotEqual(ob1, ob2)
        # checking if the two dicts are equal
        self.assertEqual(ob_dict, ob2.to_dict())

    class TestUser_instantiation(unittest.TestCase):
        """Unittests for testing instantiation of the User class."""
    
        def test_no_args_instantiates(self):
            self.assertEqual(User, type(User()))
    
        def test_new_instance_stored_in_objects(self):
            self.assertIn(User(), models.storage.all().values())
    
        def test_id_is_public_str(self):
            self.assertEqual(str, type(User().id))
if __name__ == '__main__':
    unittest.main()