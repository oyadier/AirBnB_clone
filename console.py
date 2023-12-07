#!/usr/bin/python3
"""The Command Line Interpreter."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class that contains the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Function handle end of file character"""

        print()
        return (True)

    def do_quit(self, line):
        """Quit command to exit the program"""

        return (True)

    def emptyline(self):
        """Function that does nothing on ENTER."""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
