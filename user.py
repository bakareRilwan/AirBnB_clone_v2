#!/usr/bin/python3
"""The interactive console for Admimistrative use"""


import cmd


class HBNBCommand(cmd.Cmd):
    """A Console class that inherits from cmd"""
    prompt = '(hbnb) '
    class_names = ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit comand to exit the program"""
        print()
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """create: Creates a new instance of BaseModel, saves it
        (to the JSON file)and prints the id"""
        arg = args.split()
        print(arg)
        for i in arg:
            print(i.split("="))
#        for key, in arg:
 #           print(key.spilt())



if __name__ == '__main__':
    HBNBCommand().cmdloop()
