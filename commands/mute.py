from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import colorize, Colors


class Mute(Command):
    name = 'mute'
    pattern = 'mute'
    example = ('mute', 'm',)
    description = 'Mute current track.'

    @staticmethod
    def handle(self, *args):
        if self.player:
            self.player.mute()
            return self.INDENT + colorize(Colors.GREEN, 'Track muted.')
        return self.INDENT + colorize(Colors.RED, 'No active players found.')


class M(Mute):
    name = 'm'
    pattern = 'm'
    example = ('m', 'mute',)
    show_in_main_help = False
