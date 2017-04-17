from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import render, colorize, Colors


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

        header = render('\n' + self.INDENT +
                        '{{y}}--- GENRES ----------------------------------------------------{{e}}' +
                        '\n\n' + self.INDENT)

        footer = render('\n\n' + self.INDENT +
                        '{{y}}Start listening by typing{{e}} play {genre} {{y}}command: {{e}}play kpop\n')

        if arg == 'withintro':
            header = self.intro + header
            footer = render('\n' + self.INDENT +
                            '{{l}}... {{e-y}}Show more available genres via{{e}} genres {{y}}command{{e}}') + footer

            titles_keys = titles_keys[:5]  # Trim titles

        if not titles:
            return header + \
                   colorize(Colors.RED, 'Genres list is empty. Seems API isn\'t available. Please, try again later.\n')

        return header + ('\n' + self.INDENT).join(
            colorize(Colors.LIME, k + ' - ') +
            colorize(Colors.LIME, ', ').join(titles[k]) for k in titles_keys
        ) + footer
