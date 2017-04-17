from __future__ import unicode_literals, absolute_import

from .base import Command
from utils.colorize import render


class Help(Command):
    name = 'help'
    pattern = 'help {cmd}'
    example = ('help', 'help play', 'help i',)
    description = 'Lists all available commands or shows detailed info about selected command.'

    @staticmethod
    def handle(self, *args):
        arg = args[0] if args else ''

        if arg:
            for command in self.commands:
                if arg == command.name:
                    return command.help()
            return render(self.INDENT + '{{r}}Command{{e-y}} '+ arg +
                          ' {{e-r}}not found. You can use{{e}} help {{r}}command to see all available commands.{{e}}')
        else:
            main_help = ''
            for command in self.commands:
                main_help += command.one_line_help()
            return main_help
