from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import colorize, Colors


class Unmute(Command):
    name = 'unmute'
    pattern = 'unmute'
    example = ('unmute', 'um',)
    description = 'Unmute current track.'

    @staticmethod
    def handle(self, *args):
        if self.player:
            self.player.unmute()
            return self.INDENT + colorize(Colors.GREEN, 'Track unmuted.')
        return self.INDENT + colorize(Colors.RED, 'No active players found.')


class Um(Unmute):
    name = 'um'
    pattern = 'um'
    example = ('um', 'unmute',)
    show_in_main_help = False
