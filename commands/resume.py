from __future__ import unicode_literals, absolute_import

from .base import Command


class Resume(Command):
    name = 'resume'
    pattern = 'resume'
    example = ('resume',)
    description = 'Resume paused playback.'

    @staticmethod
    def handle(*args):
        print('debug: resume command output')
