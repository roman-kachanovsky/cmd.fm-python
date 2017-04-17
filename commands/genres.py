from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import colorize, Colors


class Genres(Command):
    name = 'genres'
    pattern = 'genres'
    example = ('genres',)
    description = 'Lists all available genres.'

    @staticmethod
    def handle(self, *args):
        arg = args[0] if args else ''

        titles = self.client.genres_titles

        header = '\n' + self.INDENT + \
                 colorize(
                     Colors.YELLOW,
                     '--- GENRES ----------------------------------------------------'
                 ) + '\n\n' + self.INDENT

        if arg == 'withintro':
            header = self.intro + header

        footer = '\n\n' + self.INDENT + \
                 colorize(Colors.YELLOW, 'Start listening by typing ') + \
                 'play {genre}' + \
                 colorize(Colors.YELLOW, ' command: ') + \
                 'play KPop\n'

        return header + ('\n' + self.INDENT).join(
            colorize(Colors.GREEN, k + ' - ') +
            colorize(Colors.GREEN, ', ').join(titles[k]) for k in sorted(titles.keys())
        ) + footer
