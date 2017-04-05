from __future__ import unicode_literals, absolute_import

from .base import Command


class Pause(Command):
    name = 'pause'
    pattern = 'pause'
    example = ('pause',)
    description = 'Pause playback.'

    @staticmethod
    def handle(*args):
        print('debug: pause command output')
