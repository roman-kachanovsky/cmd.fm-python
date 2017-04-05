from __future__ import unicode_literals, absolute_import

from .base import Command


class Next(Command):
    name = 'next'
    pattern = 'next'
    example = ('next', 'skip',)
    description = 'Skips next track.'

    @staticmethod
    def handle(self, *args):
        return 'debug: next/skip command output'


class Skip(Next):
    name = 'skip'
    pattern = 'skip'
    example = ('skip', 'next',)
    show_in_main_help = False
