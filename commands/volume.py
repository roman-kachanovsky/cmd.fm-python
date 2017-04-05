from __future__ import unicode_literals, absolute_import

from .base import Command


class Volume(Command):
    name = 'volume'
    pattern = 'volume {n}'
    example = ('volume', 'v', 'vol',)
    description = 'Set volume level in percentage.'

    @staticmethod
    def handle(self, *args):
        return 'debug: volume/v/vol command output'


class V(Volume):
    name = 'v'
    pattern = 'v {n}'
    example = ('v', 'volume', 'vol',)
    show_in_main_help = False


class Vol(Volume):
    name = 'vol'
    pattern = 'vol {n}'
    example = ('vol', 'v', 'volume',)
    show_in_main_help = False
