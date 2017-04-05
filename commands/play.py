from __future__ import unicode_literals, absolute_import

from .base import Command


class Play(Command):
    name = 'play'
    pattern = 'play {o}'
    example = ('play chillout', 'play username/playlist', 'p madonna',)
    description = 'Use this command to play genres and resume paused track.'

    @staticmethod
    def handle(*args):
        return 'debug: play/p command output'


class P(Play):
    name = 'p'
    pattern = 'p {0}'
    example = ('p chillout', 'p username/playlist', 'play madonna',)
    show_in_main_help = False
