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
            # TODO: Check here if we have paused stream and resume it instead choosing of random genre
            # Pick random genre
            self.stdout_print(self.INDENT + colorize(Colors.GRAY, 'Pick random genre...'))
            arg = random.choice([genre.get('title', '') for genre in self.client.genres])

        genre = self.client.search_genre(arg)
        genre_id = genre.get('id') if genre else None

        if genre_id is None:
            return self.INDENT + colorize(Colors.RED, 'Genre ') + arg + colorize(Colors.RED, ' not found.')

        self.stdout_print(self.INDENT + colorize(Colors.GREEN, 'Tuning in...'))
        self.stdout_print(self.INDENT + colorize(Colors.GREEN, 'Starting genre: ') + genre.get('title', ''))

        stream = self.client.get_stream(genre_id)

        if not stream:
            return self.INDENT + colorize(Colors.RED, 'No active stations found... Please, try another genre.')
        # TODO: Start playing here...
        return self.INDENT + colorize(Colors.BLUE, '\u25B6 ' + self.client.active_station['name'])


class P(Play):
    name = 'p'
    pattern = 'p {genre}'
    example = ('p chillout', 'play jazz',)
    show_in_main_help = False
