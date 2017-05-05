from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import colorize, Colors


class Resume(Command):
    name = 'resume'
    pattern = 'resume'
    example = ('resume',)
    description = 'Resume paused playback.'

    @staticmethod
    def handle(self, *args):
        if self.player:
            if self.player.is_playing:
                return self.INDENT + colorize(Colors.RED, 'Track is already playing.')
            elif self.player.is_paused:
                self.player.play()
                return self.INDENT + colorize(Colors.BLUE, '\u25B6 ' + self.client.active_station['name'])
        return self.INDENT + colorize(Colors.RED, 'No active players found.')
