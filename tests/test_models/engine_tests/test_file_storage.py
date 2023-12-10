from models import base_model as bm
from models.engine import file_storage as storage
from string import ascii_letters as ASCII
import random
import unittest
import sys, os,json

class TestInstant(unittest.TestCase):

    def test_instance(self):
        """test_instance
            check if the instance is from the FileStorages
            EXPECTATION: TRUE :)
        """
        self.assertIsInstance(storage.FileStorage() , storage.FileStorage)

class TestFunctional(unittest.TestCase):

    @classmethod
    def delete_file_json(cls):
        os.remove(os.path.abspath("./models/engine/file.json"))
    @classmethod
    def create_file_jsoon(cls):
        with open(os.path.abspath("./models/engine/file.json"), 'w') as file:
            pass

    def test_instences_must_equal_the_stored_dict(self):
        """test_instences_must_equal_the_stored_dict
            testing to see if the number of instences equal
            to the len of the dict of FileStorage
            EXPECATION: the lenghts must be equal
        """
        TestFunctional.create_file_jsoon()
        # let's create some BaseModel instances
        b1 = bm.BaseModel()
        b2 = bm.BaseModel()
        b3 = bm.BaseModel()
        b4 = bm.BaseModel()
        b5 = bm.BaseModel()
        b6 = bm.BaseModel()
        # check if the lenght of the dict in the storage equal to the
        # lenght of instances we've creater (6)
        self.assertEqual(len(storage.FileStorage().all()), 6)
        TestFunctional.delete_file_json()
        # flush the dict
        storage.FileStorage().flush()
    def test_trying_to_save(self):
        """test_trying_to_save
            trying to save the instances
            EXPECTATION: we're expecting the the function to save the
                        instances as dicts into the json file
        """
        # make sure the json file exist
        TestFunctional.create_file_jsoon()
        # let's create some BaseModel instances
        b1 = bm.BaseModel()
        b2 = bm.BaseModel()
        b3 = bm.BaseModel()
        b4 = bm.BaseModel()
        b5 = bm.BaseModel()
        b6 = bm.BaseModel()

        # and now let's reload the instances from  the json file
        storage.FileStorage().reload()

        # let's check if the lenght of the reloaded dict equals to the
        # lenght of instances we've created (6)
        self.assertEqual(len(storage.FileStorage().all()),6)
        TestFunctional.delete_file_json()
        # flush the dict
        storage.FileStorage().flush()

    def test_the_dict_loaded_are_instance_of_BaseModel(self):
        """test_the_dict_loaded_are_instance_of_BaseModel
            this function tests if every value in the dict of
            FileStorage is an instance of BaseModel
            EXPECTATION: every object inside of the dict is indeed
                        a BaseModel instance
        """
        # make sure the json file exist
        TestFunctional.create_file_jsoon()
        # let's create some BaseModel instances
        b1 = bm.BaseModel()
        b2 = bm.BaseModel()
        b3 = bm.BaseModel()
        b4 = bm.BaseModel()
        b5 = bm.BaseModel()
        b6 = bm.BaseModel()

        # get the all dict
        the_dict = storage.FileStorage().all()
        # check if every value in the dict is a BaseModel instantest_the_dict_loaded_are_instance_of_BaseModelce
        for key in the_dict.keys():
            self.assertIsInstance(the_dict[key],bm.BaseModel)
        # delete the json file
        TestFunctional.delete_file_json()
        # flush the dict
        storage.FileStorage().flush()


    def test_the_dict_reloaded_are_instance_of_BaseModel(self):
        """test_the_dict_reloaded_are_instance_of_BaseModel
            this function tests if every value in the dict of
            FileStorage is an instance of BaseModel
            EXPECTATION: every object inside of the dict is indeed
                        a BaseModel instance
        """
        # make sure the json file exist
        TestFunctional.create_file_jsoon()
        # let's create some BaseModel instances
        b1 = bm.BaseModel()
        b2 = bm.BaseModel()
        b3 = bm.BaseModel()
        b4 = bm.BaseModel()
        b5 = bm.BaseModel()
        b6 = bm.BaseModel()

        # reload the dict
        storage.FileStorage().reload()
        # get the all dict
        the_dict = storage.FileStorage().all()
        # check if every value in the dict is a BaseModel instance
        for key in the_dict.keys():
            self.assertIsInstance(the_dict[key],bm.BaseModel)
        # delete the json file
        TestFunctional.delete_file_json()
        # flush the dict
        storage.FileStorage().flush()
if __name__ == '__main__':
    unittest.main()



