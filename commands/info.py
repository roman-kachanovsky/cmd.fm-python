from __future__ import unicode_literals, absolute_import

from .base import Command


class Info(Command):
    name = 'info'
    pattern = 'info'
    example = ('info', 'i', 'information',)
    description = 'Shows more information about current track.'

    @staticmethod
    def handle(*args):
        return 'debug: i/info/information command output'


class I(Info):
    name = 'i'
    pattern = 'i'
    example = ('i', 'info', 'information',)
    show_in_main_help = False


class Information(Info):
    name = 'information'
    pattern = 'information'
    example = ('information', 'i', 'info',)
    show_in_main_help = False
