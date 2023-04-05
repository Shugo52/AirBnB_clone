#!/usr/bin/python3
""" Console Module"""

import cmd
from models.base_model import BaseModel
import models
import shlex


class HBNBCommand(cmd.Cmd):
    """ Defines the 'HBNBCommand' class
    This class inherits from 'cmd.Cmd

    Attributes:
        prompt: prompt string
        __classes: list of all classes
    """
    prompt = "(hbnb) "
    __classes = [
        "BaseModel",
    ]

    def do_create(self, args):
        """ Usage: create <class>
        Creates a new class instance and prints its id
        """
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist")
        else:
            print(eval(arg[0])().id)
            models.storage.save()

    def do_show(self, args):
        """Usage: show <class> <id>
        Prints string representation of instance of class
        based on id"""
        arg = shlex.split(args)
        all_objs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in all_objs.keys():
            print("** no instance found **")
        else:
            print(all_objs[f"{arg[0]}.{arg[1]}"])

    def do_destroy(self, args):
        """Usage: destroy <class> <id>
        Delete a class instance based on id
        """
        arg = shlex.split(args)
        all_objs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in all_objs.keys():
            print("** no instance found **")
        else:
            del all_objs[f"{arg[0]}.{arg[1]}"]
            models.storage.save()

    def do_all(self, args):
        """Usage: all <class>  or  all
        Prints string representation of all instances of available"""
        arg = shlex.split(args)
        all_objs = models.storage.all()
        if len(arg) == 0:
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                print(obj)
        elif arg[0] and arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for arg[0] in all_objs.keys():
                print(all_objs[arg[0]])

    def do_update(self, args):
        """Usage:
        update <class name> <id> <attribute name> '<attribute value>'
        Updates an instance based on class id by adding or updating
        attributes"""
        arg = shlex.split(args)[0:4]
        all_objs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif f"{arg[0]}.{arg[1]}" not in all_objs.keys():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            updateDict = all_objs[f"{arg[0]}.{arg[1]}"]
            updateDict.__dict__[arg[2]] = arg[3]
            updateDict.save()

    def do_quit(self, line):
        """ Quit command to exit the program
        """
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """ End of line method"""
        print('')
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
