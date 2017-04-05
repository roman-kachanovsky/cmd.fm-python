#!/usr/bin/env python

from __future__ import unicode_literals, print_function

import cmd

from commands import commands
from utils.colorize import colorize, Colors


class Fm(cmd.Cmd):
    prompt = colorize(Colors.LIME, '$ fm ')
    intro = """
                 _   ___
     ___ _____ _| | |  _|_____
    |  _|     | . |_|  _|     |
    |___|_|_|_|___|_|_| |_|_|_|
    ---------------------------------------------------------------
    {}: play chillout{} play madonna {}
    {} help {}
    """.format(
        colorize(Colors.YELLOW, 'Welcome to cmd.fm! Use play command to begin listening.\n    For example'),
        colorize(Colors.YELLOW, ','),
        colorize(Colors.YELLOW, 'etc...'),
        colorize(Colors.GRAY, 'You can use'),
        colorize(Colors.GRAY, 'command to see all cmd.fm commands.')
    )

    def __init__(self, *args, **kwargs):
        for command in commands:
            setattr(Fm, *command.bind_handler())
            setattr(Fm, *command.bind_help())
        cmd.Cmd.__init__(self, *args, **kwargs)

    def do_help(self, arg):
        if arg:
            try:
                fn = getattr(self, 'help_' + arg)
            except AttributeError:
                print(
                    colorize(Colors.RED, 'Command ') + colorize(Colors.YELLOW, arg)
                    + colorize(Colors.RED, ' not found. You can use ')
                    + 'help' + colorize(Colors.RED, ' command to see all available commands.')
                )
                return
            fn()
        else:
            for command in commands:
                print(command.one_line_help(), end='')

    def default(self, arg):
        print(colorize(Colors.RED, 'Unknown command ') + arg)

    def emptyline(self):
        # Do not repeat last used command when user entered empty line
        pass


if __name__ == '__main__':
    Fm().cmdloop()
