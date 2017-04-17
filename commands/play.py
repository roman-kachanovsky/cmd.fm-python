from __future__ import unicode_literals, absolute_import

import random

from .base import Command
from utils.colorize import colorize, Colors


class Play(Command):
    name = 'play'
    pattern = 'play {genre}'
    example = ('play chillout', 'p jazz',)
    description = 'Use this command to play genres and resume paused track.'

    @staticmethod
    def handle(self, *args):
        arg = args[0] if args else ''

        if not arg:
            # Pick random genre
            arg = random.choice([genre.get('title', '') for genre in self.client.genres])

        genre_id = self.client.search_genre(arg)

        if genre_id is None:
            return self.INDENT + colorize(Colors.RED, 'Genre ') + arg + colorize(Colors.RED, ' not found.')
        return str(genre_id)


class P(Play):
    name = 'p'
    pattern = 'p {genre}'
    example = ('p chillout', 'play jazz',)
    show_in_main_help = False
