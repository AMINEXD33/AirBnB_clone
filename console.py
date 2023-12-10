#!/usr/bin/python3
"""Defines the HBnB console."""
import shlex
import os
import cmd
import datetime
import re
from models import storage
from models import base_model
from models.engine import file_storage
from models.base_model import BaseModel
from models import user
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

"""Classes"""
BaseModel = base_model.BaseModel
User = user.User


    
class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    prompt = "(hbnb) "
    __classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            ]
    def default(self, arg):
        """default
            this function is a mapper, so it can map the old
            commands like(all, show, destroy, update) and the new
            structured commands (<classname>.all(), <classname>.count(),
            <classname>.count)
            
            NOTE: it works by simply reusing the old methods for the new
            commands
        """
        new_commands_stage1 = re.compile('^(\w+)\.(\w+)(\(["\w\d\-\s,]*\))$')
        new_commands_stage2 = re.compile\
            ('^(\w+)\.(all|create|count|destroy|update|show)(\(["\w\d\-\s,]*\))$')
        # check if it's a new command, <classname>.something()
        if (re.match(new_commands_stage1, arg)):
            # check for the validity of the action all,create....
            if not (re.match(new_commands_stage2, arg)):
                print ("*** Unknown syntax: ",arg)
                return
            
            # find all in the regex
            tmp_command = re.findall(new_commands_stage2, arg)

            # validate if the class exists
            if (tmp_command[0][0] in HBNBCommand.__classes):
                
                # validate if the action is valid
                if (re.match(new_commands_stage2, arg)):
                    self.action_mapper(tmp_command)
                else:
                    print ("*** Unknown syntax: ",tmp_command[0][1])
                    
            else:
                print("** class doesn't exist **")
        else:
            # call the old default. so our cmd, would convert to 
            # old behavior when the new commads are not passed
            super().default(arg)

    def action_mapper(self, arg_list):
        """action_mapper
            help the default map an action to it's proper function
            args:
                arg_list : the a list containing all args
        """
        # formating the arg_list
        # Explaination: the arg_list passed from the default function
        # is in this format [('command', 'action', '(arg1, arg2,....)')]
        # so we need to trime it and convert it to an str of this format
        # <command action "arg1 arg2 ....">, bc out early methods can only
        # handle this format

        def trime_class_name_action_and_args(arg_list):
            """trime_class_name_action_and_args
            trime the arg_list and split them into two variables
            1 classname AND action
            2 arguments
            args:
                args_list: the argument list
            """
            trimed_str = [str(arg_list[0][0]),str(arg_list[0][1])]
            # get the splited args "(arg1, arg2..)"--> ["arg1","arg2"...]
            args = arg_list[0][2].strip("()").split(",")
            
            trimed_agrs = ""
            # append the args to our  trimed_args
            for x in args:
                trimed_agrs+=f"{x} "
            return trimed_str, trimed_agrs
        
        list_,trimed_args = trime_class_name_action_and_args(arg_list)
        
        if (list_[1] == "all"):
            # CLASSNAME all
            command = f"{list_[0]} {list_[1]}"
            self.do_all(command)

        elif (list_[1] == "update"):
            # CLASSNAME id args
            command = f"{list_[0]} {trimed_args}"
            self.do_update(command)

        elif (list_[1] == "count"):
            # reload the json objects into file storage
            file_storage.FileStorage().reload()
            # get the dict
            reloaded_dict = file_storage.FileStorage().all()            
            count = 0
            for key in reloaded_dict.keys():
                # split the key , Note: key = <classname>.id
                splited_key = key.split(".")
                if (splited_key[0] == list_[0]):
                    count+=1
            print (count)

        elif (list_[1] == "destroy"):
            # class ID
            command = f"{list_[0]} {trimed_args}"
            self.do_destroy(command)

        elif(list_[1] == "show"):
            # class i
            command = f"{list_[0]} {trimed_args}"
            self.do_show(command)

        elif (list_[1] == "create"):
            # class
            command = f"{list_[0]}"
            self.do_create(command)
        
    def do_count(self, arg):
        """count the number of a class , if it doesn't exist it will print 0"""
        # get the list of arguments
        args_list = self.parse_args(arg)
        if (len(args_list) < 1):
            print (0)
            return
        # reload the json objects into file storage
        file_storage.FileStorage().reload()
        # get the dict
        reloaded_dict = file_storage.FileStorage().all()            
        count = 0
        for key in reloaded_dict.keys():
            # split the key , Note: key = <classname>.id
            splited_key = key.split(".")
            if (splited_key[0] == args_list[0]):
                count+=1
        print (count)
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_destroy(self, arg):
        """
        deletes an instance based on the class name and id
        """
        # get the list of arguments
        args_list = self.parse_args(arg)
        len_ = len(args_list)
        # check if the number of args are valid
        # print a message as needed
        if (len_ == 0):
            print("** class name missing **")
            return
        elif (len_ == 1):
            print("** instance id missing **")
            return
        del len_  # not needed
        if (args_list[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **",args_list[0])
            return
        # reload the json objects into file storage
        file_storage.FileStorage().reload()
        # get the dict
        reloaded_dict = file_storage.FileStorage().all()
        # two flags to keep track of
        # 1 > is the instance found or not
        # 2 > if the instance id found or not
        instance_found = False
        instance_id_found = False

        for key in reloaded_dict.keys():
            # split the key , Note: key = <classname>.id
            splited_key = key.split(".")

            # check if module exists in the key
            if (splited_key[0] == args_list[0]):
                instance_found = True

                # checks if the id exists in the key
                if (splited_key[1] == args_list[1]):
                    # delets the targeted key
                    file_storage.FileStorage().flush_key(key)
                    # save changes
                    file_storage.FileStorage().save()
                    file_storage.FileStorage().reload()

                    return  # both are found and deletion is a success
                else:
                    print("** no instance found **")
                    return 
                    
        if (instance_found is True and instance_id_found is False):
            print("** no instance found **")
            return

    def do_all(self, arg):
        """show all the instances stored
        """
        # get the list of arguments
        args_list = self.parse_args(arg)

        # reload the json objects into file storage
        file_storage.FileStorage().reload()
        # get the dict
        reloaded_dict = file_storage.FileStorage().all()
        result_list = []
        if (len(args_list) >= 1):
            if (args_list[0] not in HBNBCommand.__classes):
                print("** class doesn't exist **")
                return
            for key in reloaded_dict.keys():
                # split the key , Note: key = <classname>.id
                splited_key = key.split(".")
                if (splited_key[0] == args_list[0]):
                    result_list.append(str(reloaded_dict[key]))
            # if no reslut is found and a module is passed as arg
            if (len(result_list) == 0):
                return
            else:
                print(result_list)
                return
        for _, value in reloaded_dict.items():
            result_list.append(str(value))
        if (len(result_list) >= 1):
            print(result_list)

    def parse_args(self, args):
        """parse_args
        gets a str object (args) parse it and return a list
        of args
        """
        result = shlex.split(args)
        try :
            return result
        except Exception:
            print ("*** Unknown syntax: ",args)


    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        # get the list of arguments
        args_list = self.parse_args(arg)

        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")  # Fix: Correct the error message
        else:
            print(eval(args_list[0])().id)
            storage.save()
            storage.reload()

    def do_show(self, arg):
        """Usage: show <class> <id>
        Display the string representation of an instance
        based on the class name
        """
        # get the list of arguments
        args_list = self.parse_args(arg)

        objdict = storage.all()
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args_list[0], args_list[1])])

    def do_update(self, arg):
        """
        update the attribute of an instance
        """

        argl = self.parse_args(arg)
        storage.reload()
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(argl) == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return
        if len(argl) == 2:
            print("** attribute name missing **")
            return
        if len(argl) == 3:
            print("** value missing **")
            return
        # get the object
        obj = objdict[(f"{argl[0]}.{argl[1]}")]
        old_key = f"{argl[0]}.{argl[1]}"

        try:
            setattr(obj, argl[2], argl[3])
        except Exception:
            pass
        # flush the old obj
        storage.flush_key(old_key)
        # create the new modified instence
        obj.updated_at = datetime.datetime.today()
        storage.new(obj)
        # save the new instance
        storage.save()
        storage.reload()

    '''#FUNCTION ONLY FOR DEBUGGING
    def do_clear(self, args):
        """
        clear the terminal
        """
        # clear for windows machines
        try :
            os.system("cls")
        except:
            pass
        # clear for linux machines
        try:
            os.system("clear")
        except:
            pass
    def do_flushALL(self, args):
        """
        flush the dict in the storage, meaning
        the dict is going to be set to empty
        """
        message = "are you sure you wan't to flush the dict Yes/other(NO)"
        print (message)
        if (input("> ") == "Yes"):
            storage.flush()
            storage.save()
            storage.reload()
    '''

if __name__ == "__main__":
    HBNBCommand().cmdloop()
