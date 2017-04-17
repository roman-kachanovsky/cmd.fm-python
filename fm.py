#!/usr/bin/env python

from __future__ import unicode_literals

import cmd
import os

from commands import commands
from utils.colorize import colorize, Colors
from client.client import DirbleClient


class Fm(cmd.Cmd):
    INDENT = ' ' * 4

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

    @classmethod
    def _bind_handler(cls, cmd):
        def fn(self, *args):
            self.stdout_print(cmd.handle(self, *args))
        setattr(cls, 'do_' + cmd.name, fn)

    @classmethod
    def _bind_help(cls, cmd):
        def fn(self, *args):
            self.stdout_print(cmd.help())
        setattr(cls, 'help_' + cmd.name, fn)

    def __init__(self, client=None, *args, **kwargs):
        for command in commands:
            Fm._bind_handler(command)
            Fm._bind_help(command)

        self.client = client
        cmd.Cmd.__init__(self, *args, **kwargs)
        self.commands = commands
        self.intro = self.onecmd('genres withintro')

    def stdout_print(self, text, end='\n'):
        self.stdout.write(text + end)

    def default(self, arg):
        self.stdout_print(colorize(Colors.RED, 'Unknown command ') + arg)

    def emptyline(self):
        # Do not repeat last used command when user entered empty line
        pass


if __name__ == '__main__':
    api_key = os.environ.get('DIRBLE_API_KEY')

    if api_key:
        client = DirbleClient(api_key)
        Fm(client=client).cmdloop()
    else:
        print(colorize(Colors.RED, 'Please, specify your ') +
              'DIRBLE_API_KEY' +
              colorize(Colors.RED, ' in environment variables.'))
