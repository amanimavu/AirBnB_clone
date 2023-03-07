#!/usr/bin/python3
"""
module: base_model
resourses: BaseModel class
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
    This class defines all common attributes and
    methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        This method automatically initilizes instance
        variables to a newly created instance.

        Contains logic for when arguments are supplied
        when creating the new instance and when no
        arguments are used.
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        This method defines the string representation
        of an instance when used with the str() and
        print() methods
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__
                )

    def save(self):
        """
        This method is used to save created instances
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        This method returns a dictionary of attributes for
        a particular instance
        """
        attr_dict = self.__dict__
        attr_dict["__class__"] = self.__class__.__name__
        attr_dict["created_at"] = self.created_at.isoformat()
        attr_dict["updated_at"] = self.updated_at.isoformat()
        return attr_dict
