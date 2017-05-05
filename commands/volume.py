from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import colorize, Colors


class Volume(Command):
    name = 'volume'
    pattern = 'volume {n}'
    example = ('volume 45', 'v 45', 'vol 45',)
    description = 'Set volume level in percentage.'

    @staticmethod
    def handle(self, *args):
        if self.player:
            arg = args[0] if args else ''

            if not arg:
                return self.INDENT + colorize(Colors.GREEN, 'Current volume is ') + str(self.player.get_volume())

            try:
                self.player.set_volume(int(arg))
            except ValueError:
                return self.INDENT + colorize(Colors.RED, 'Volume value ') + arg + \
                       colorize(Colors.RED, ' isn\'t valid.')
            return self.INDENT + colorize(Colors.GREEN, 'Set volume to ') + arg
        return self.INDENT + colorize(Colors.RED, 'No active players found.')


class V(Volume):
    name = 'v'
    pattern = 'v {n}'
    example = ('v 45', 'volume 45', 'vol 45',)
    show_in_main_help = False


class Vol(Volume):
    name = 'vol'
    pattern = 'vol {n}'
    example = ('vol 45', 'v 45', 'volume 45',)
    show_in_main_help = False
