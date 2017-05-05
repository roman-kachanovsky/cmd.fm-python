from __future__ import unicode_literals, absolute_import

import random
import time

from .base import Command
from utils.colorize import colorize, Colors
from player.player import Player


class Play(Command):
    name = 'play'
    pattern = 'play {genre}'
    example = ('play chillout', 'p jazz',)
    description = 'Use this command to play genres and resume paused track.'

    @staticmethod
    def handle(self, *args):
        arg = args[0] if args else ''

        if not arg:
            if self.player and self.player.is_paused:
                self.player.play()
                return self.INDENT + colorize(Colors.BLUE, '\u25B6 ' + self.client.active_station['name'])

            self.stdout_print(self.INDENT + colorize(Colors.GRAY, 'Pick random genre...'))
            arg = random.choice([genre.get('title', '') for genre in self.client.genres])

        genre = self.client.search_genre(arg)
        genre_id = genre.get('id') if genre else None

        if genre_id is None:
            return self.INDENT + colorize(Colors.RED, 'Genre ') + arg + colorize(Colors.RED, ' not found.')

        self.stdout_print(self.INDENT + colorize(Colors.GREEN, 'Tuning in...'))
        self.stdout_print(self.INDENT + colorize(Colors.GREEN, 'Starting genre: ') + genre.get('title', ''))

        num_of_tries = 0
        while num_of_tries < 3:
            num_of_tries += 1
            stream = self.client.get_stream(genre_id, renew_active_station=True)

            if not stream:
                return self.INDENT + colorize(Colors.RED, 'No active stations found... Please, try another genre.')

            if self.player:
                self.player.stop()
            self.player = Player(stream)
            self.player.play()

            num_of_checks = 0
            while num_of_checks < 5:
                num_of_checks += 1
                time.sleep(1)
                if self.player.is_playing:
                    return self.INDENT + colorize(Colors.BLUE, '\u25B6 ' + self.client.active_station['name'])
        return self.INDENT + colorize(Colors.RED, 'No active stations found... Please, try another genre.')


class P(Play):
    name = 'p'
    pattern = 'p {genre}'
    example = ('p chillout', 'play jazz',)
    show_in_main_help = False
