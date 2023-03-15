#!/usr/bin/python3
"""
module: console
resource: a class called HBNBCommand
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class has been written to implement the console.
    It inherits from the Cmd class(super class) contained
    in the cmd module.

    This class contains methods such as do_quit, do_EOF,
    do_create, do_all, do_update, etc that correspond to
    the permitted commands that can be used for the console
    program such as quit, EOF, create, all, update, etc.
    """
    prompt = '(hbtn): '

    def do_quit(self, line):
        """
        Quit is used to exit the interpreter
        """
        return " "

    def do_EOF(self, line):
        """
        This command is used to exit the interpreter
        """
        return " "

    def emptyline(self):
        """
        Overide the default behaviour of an empty
        line input
        """
        return ""

    def help_quit(self):
        """
        This method is used to avail the documentation
        for the quit command
        """
        print("Quit is used to exit the interpreter")

    def help_EOF(self):
        """
        This ethod is used to avail the documentation
        for the EOF command
        """
        print("EOF is used to exit the interpreter")

    def help_create(self):
        """
        This method is used to avail the documentation
        for the create command
        """
        print("Creates an instance of a specified class")

    def do_create(self, cls):
        """
        This method defines how an instance will be created
        from the console command create.

        If the <class> is not specified upon using the
        create command an error message will be issued

        If the <class> specified doesn't exist, then
        an error message will be issued
        """
        if not cls:
            print("** class name missing **")
            return
        try:
            Model = globals()[cls]
        except KeyError:
            print("** class doesn't exist **")
        else:
            obj = Model()
            obj.save()
            print(obj.id)

    @staticmethod
    def parse_cmd_line(ln):
        """
        This is a helper method used to parse the
        arguments issued by the user and manage
        some of the errors
        """
        args = ln.split(" ")
        if not args[0]:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        else:
            try:
                Id = args[1]
            except IndexError:
                print("** instance id missing **")
                return
            else:
                return "{}.{}".format(args[0], Id)

    def do_destroy(self, line):
        """
        This method defines how an instance is deleted
        from the console program. It corresponds to the
        command: destroy <id>
        """
        object_id = HBNBCommand.parse_cmd_line(line)
        if object_id:
            all_objects = storage.all()
            try:
                del(all_objects[object_id])
            except KeyError:
                print("** no instance found **")
                return
            else:
                storage.save()

    def do_show(self, line):
        """
        Defines how a particular instance that has been
        created will be displayed by the console. It
        corresponds to the command: show <class> <id>.
        It also defines how errors are handled the the
        show command is used wrongly
        """
        object_id = HBNBCommand.parse_cmd_line(line)
        if object_id:
            all_objects = storage.all()
            try:
                obj = all_objects[object_id]
            except KeyError:
                print("** no instance found **")
                return
            else:
                print(obj)
                return

    def do_all(self, line):
        """
        This method defines how saved instances will be
        displayed. It corresponds to the console command
        all [class]. When the command all is used without
        any argument it displays all created instances.
        However, when the optional argument is given, then
        it displays all instances of the specified class.
        """
        result_str = ""
        all_objects = storage.all()
        if not line:
            for value in all_objects.values():
                result_str += str(value)
            print([result_str])
        else:
            try:
                cls = globals()[line]
            except KeyError:
                print("** class doesn't exist **")
                return
            else:
                for key, value in all_objects.items():
                    if key.startswith(cls.__name__):
                        result_str += str(value)
            print([result_str])

    def do_update(self, line):
        """
        This method corresponds to the console command
        update and defines how to modified an instance
        already created with a new attribute. It handles
        errors when the update command is used wrongly.

        The update command is only able to include one
        attribute at a time to an already created instance.
        """
        object_id = HBNBCommand.parse_cmd_line(line)
        if object_id:
            all_objects = storage.all()
            try:
                obj = all_objects[object_id]
            except KeyError:
                print("** no instance found **")
                return
            else:
                args = line.split()
                try:
                    attr_name = args[2]
                except IndexError:
                    print("** attribute name missing **")
                    return
                else:
                    try:
                        attr_value = args[3]
                    except IndexError:
                        print("** value missing **")
                        return
                    else:
                        if attr_value.startswith('"'):
                            obj.__dict__[attr_name] = attr_value.strip('"')
                        else:
                            if "." in attr_value:
                                obj.__dict__[attr_name] = float(attr_value)
                            else:
                                obj.__dict__[attr_name] = int(attr_value)
                        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
