from __future__ import unicode_literals, absolute_import

import sys

from .base import Command


class Quit(Command):
    name = 'quit'
    pattern = 'quit'
    example = ('quit', 'q',)
    description = 'Close cmd.fm and turn off music.'

    @staticmethod
    def handle(self, *args):
        if self.player:
            self.player.stop()
        sys.exit()


class Q(Quit):
    name = 'q'
    pattern = 'q'
    example = ('q', 'quit',)
    show_in_main_help = False
