from __future__ import unicode_literals, absolute_import

from .base import Command


class Genres(Command):
    name = 'genres'
    pattern = 'genres'
    example = ('genres',)
    description = 'Lists all available genres.'

    @staticmethod
    def handle(self, *args):
        return 'debug: genres command output'
