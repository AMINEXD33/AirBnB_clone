#!/usr/bin/python3
"""The base Model"""
from datetime import datetime
import uuid
from models.engine import file_storage


class BaseModel():
    """
    BaseModel
        class containing the base module for the AirBnb project
    """
    __format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """constructor of this module
            args:
                *args : (NOT USED)
                **kwargs : if this dict is availble, the __init__
                           will initialize the object using it
                NOTE: if kwargs is empty , then the standard initialize logic
                      will be applied , see bellow
        """

        """KWARGS initializing"""
        # if kwargs are available
        if (kwargs):
            # this flag tracks if all attributes needed are available
            flag = True
            # check of the existence of the attributs in the dict
            for x in ["id", "updated_at", "created_at"]:
                if x not in kwargs:
                    flag = False  # if not then set flag = False and break
                    break
            # if flag is True (attributes are availble)
            if flag:
                # map every attribute to it's propper value
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = str(value)
                    elif key == "created_at":
                        # load the date time using the __format
                        self.created_at = \
                            datetime.strptime(str(value), BaseModel.__format)
                    elif key == "updated_at":
                        # load the date time using the __format
                        self.updated_at = \
                            datetime.strptime(str(value), BaseModel.__format)
                return  # DONE
        """STANDARD initializing"""
        # if not just create the instance the standard way
        # create id for the instance
        self.id = str(uuid.uuid4())
        # get the current time for both attributes
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        file_storage.FileStorage().new(self)

    def __SPinit__(self, **kwargs):
        """__SPinit__
        this function helps the subclasses of BaseModel set
        up their attributes with respect to the their types

        args:
            kwargs: a dict of attributes name as keys
            and there values
        """
        # deleting the already set args
        for x in ["id", "created_at", "updated_at"]:
            try:
                del kwargs[x]
            except Exception:
                pass

        # set up the other args , with respect to type
        if kwargs:
            for key, value in kwargs.items():
                if key in self.__dict__.keys():
                    type_of_attr = type(getattr(self, key))
                    try:
                        if (type_of_attr is str):
                            setattr(self, key, str(value))

                        elif (type_of_attr is int):
                            setattr(self, key, int(value))

                        elif (type_of_attr is float):
                            setattr(self, key, float(value))
                    except Exception:
                        pass

    def __str__(self):
        """__str__
            redifinition of the str method to return a dict, containing
            the id , and the self dict
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        file_storage.FileStorage().save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
