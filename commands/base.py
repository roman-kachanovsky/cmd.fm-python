from __future__ import unicode_literals

from utils.colorize import colorize, Colors


class Command(object):
    name = ''
    pattern = ''
    example = []
    description = ''
    show_in_main_help = True

    @staticmethod
    def handle(self, *args):
        raise NotImplementedError

    @classmethod
    def help(cls):
        return '    {}{}{}\n    {}'.format(
            cls.pattern,
            colorize(Colors.GRAY, ' - Example: ' if len(cls.example) == 1 else ' - Examples: '),
            colorize(Colors.GRAY, ' | ').join(cls.example),
            colorize(Colors.GREEN, cls.description)
        )

    @classmethod
    def one_line_help(cls):
        return '    {:<15} - {}{}{}\n'.format(
            cls.pattern,
            colorize(Colors.GREEN, cls.description),
            colorize(Colors.GRAY, ' Example: ' if len(cls.example) == 1 else ' Examples: '),
            colorize(Colors.GRAY, ' | ').join(cls.example)
        ) if cls.show_in_main_help else ''
