#!/usr/bin/env python

from __future__ import unicode_literals

import cmd
import os

from commands import commands
from utils.colorize import render, colorize, Colors
from client.client import DirbleClient


class Fm(cmd.Cmd):
    INDENT = ' ' * 4

    prompt = colorize(Colors.LIME, '$ fm ')
    intro = render("""
                 _   ___
     ___ _____ _| | |  _|_____
    |  _|     | . |_|  _|     |
    |___|_|_|_|___|_|_| |_|_|_|
    ---------------------------------------------------------------
    {{y}}Welcome to cmd.fm! Use{{e}} play {{y}}command to begin listening.
    For example:{{e}} play chillout{{y}}, {{e}}play dubstep {{y}}etc...
    {{g}}You can use{{e}} help {{g}}command to see all cmd.fm commands.{{e}}
    """)

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

    def __init__(self, client=None, test=False, *args, **kwargs):
        for command in commands:
            Fm._bind_handler(command)
            Fm._bind_help(command)

        self.client = client
        cmd.Cmd.__init__(self, *args, **kwargs)
        self.commands = commands
        if not test:
            self.intro = self.onecmd('genres withintro')

    def stdout_print(self, text, end='\n'):
        self.stdout.write(text + end)

    def default(self, arg):
        self.stdout_print(self.INDENT + colorize(Colors.RED, 'Unknown command ') + arg)

    def emptyline(self):
        # Do not repeat last used command when user entered empty line
        pass


if __name__ == '__main__':
    api_key = os.environ.get('DIRBLE_API_KEY')

    if api_key:
        client = DirbleClient(api_key)
        Fm(client=client).cmdloop()
    else:
        print(render('{{r}}Please, specify your{{e}} DIRBLE_API_KEY {{r}}in environment variables.{{e}}'))
