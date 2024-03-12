#!/usr/bin/env python3

import json
import datetime
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file_storage = FileStorage()

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in FileStorage.__subclasses__():
            print("** class doesn't exist **")
            return
        if cls_name == "BaseModel":
            obj = BaseModel()
        elif cls_name == "User":
            obj = User()
        else:
            obj = FileStorage.__subclasses__()[FileStorage.__subclasses__.index(cls_name)]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id."""
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        if cls_name not in FileStorage.__subclasses__():
            print("** class doesn't exist **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        if key not in FileStorage.all():
            print("** no instance found **")
            return
        print(FileStorage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_name = args[0]
        if cls_name not in FileStorage.__subclasses__():
            print("** class doesn't exist **")
            return
        obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        if key not in FileStorage.all():
            print("** no instance found **")
            return
        del FileStorage.all()[key]
        FileStorage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        if not line:
            print([str(obj) for obj in FileStorage.all().values()])
        else:
            cls_name = line.split()[0]
            if cls_name not in FileStorage.__subclasses__():
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in FileStorage.all().values() if type(obj).__name__ == cls_name])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        args = line.split()
        if len(args) < 4:
            print("** usage: update <class name> <id> <attribute name> '<attribute value>' **")
            return
        cls_name = args[0]
        if cls_name not in FileStorage.__subclasses__():
            print("** class doesn't exist **")
            return
       obj_id = args[1]
        key = f"{cls_name}.{obj_id}"
        if key not in FileStorage.all():
            print("** no instance found **")
            return
        attr_name = args[2]
        if attr_name in ["id", "createdobj_id = args[_at",1]
        key "updated_at"] = f"{cls_name}.{obj_id}"
        if key not in FileStorage.all():
            print("** no instance found **")
            return
        attr_name = args[2]
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** attribute name invalid **")
            return
        attr:
            print("** attribute name invalid **")
            return
        attr_value = " ".join(args[3:])
        setattr(FileStorage.all()[key], attr_name, attr_value)
_value = " ".join(args[3:])
        if type(FileStorage.all()[key]) == User and attr_name == "email":
            attr_value = attr_value.lower        FileStorage.save()
