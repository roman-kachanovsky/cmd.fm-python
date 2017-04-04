#!/usr/bin/env python
from __future__ import unicode_literals

import cmd
import sys

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

    def do_quit(self, line):
        sys.exit(0)


if __name__ == '__main__':
    Fm().cmdloop()
