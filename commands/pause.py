from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import colorize, Colors


class Pause(Command):
    name = 'pause'
    pattern = 'pause'
    example = ('pause',)
    description = 'Pause playback.'

    @staticmethod
    def handle(self, *args):
        if self.player:
            if self.player.is_playing:
                self.player.pause()
                return self.INDENT + colorize(Colors.GREEN, 'Track paused.')
            elif self.player.is_paused:
                return self.INDENT + colorize(Colors.RED, 'Track already paused.')
        return self.INDENT + colorize(Colors.RED, 'No active players found.')
