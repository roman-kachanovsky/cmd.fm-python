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
        titles_keys = sorted(titles.keys())

        header = '\n' + self.INDENT + \
                 colorize(
                     Colors.YELLOW,
                     '--- GENRES ----------------------------------------------------'
                 ) + '\n\n' + self.INDENT

        footer = '\n\n' + self.INDENT + \
                 colorize(Colors.YELLOW, 'Start listening by typing ') + \
                 'play {genre}' + \
                 colorize(Colors.YELLOW, ' command: ') + \
                 'play kpop\n'

        if arg == 'withintro':
            header = self.intro + header
            footer = '\n' + self.INDENT + colorize(Colors.LIME, '...') + \
                colorize(Colors.YELLOW, ' Show more available genres via ') + \
                'genres' + colorize(Colors.YELLOW, ' command') + footer

            titles_keys = titles_keys[:5]  # Trim titles

        if not titles:
            return header + \
                   colorize(Colors.RED, 'Genres list is empty. Seems API isn\'t available. Please, try again later.\n')

        return header + ('\n' + self.INDENT).join(
            colorize(Colors.LIME, k + ' - ') +
            colorize(Colors.LIME, ', ').join(titles[k]) for k in titles_keys
        ) + footer
