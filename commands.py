from __future__ import unicode_literals

import sys

from utils.colorize import colorize, Colors


class Command(object):
    name = ''
    pattern = ''
    example = []
    description = ''

    @staticmethod
    def handle(*args):
        raise NotImplementedError

    @classmethod
    def bind_handler(cls):
        def fn(*args):
            return cls.handle(*args)
        return 'do_' + cls.name, fn

    @classmethod
    def help(cls):
        print '{}{}{}\n{}'.format(
            cls.pattern,
            colorize(Colors.GRAY, ' - Example: ' if len(cls.example) == 1 else ' - Examples: '),
            colorize(Colors.GRAY, ' | ').join(cls.example),
            colorize(Colors.GREEN, cls.description)
        )

    @classmethod
    def one_line_help(cls):
        return '{:<15} - {}{}{}'.format(
            cls.pattern,
            colorize(Colors.GREEN, cls.description),
            colorize(Colors.GRAY, ' Example: ' if len(cls.example) == 1 else ' Examples: '),
            colorize(Colors.GRAY, ' | ').join(cls.example)
        )

    @classmethod
    def bind_help(cls):
        def fn(*args):
            return cls.help()
        return 'help_' + cls.name, fn


class Genres(Command):
    name = 'genres'
    pattern = 'genres'
    example = ('genres',)
    description = 'Lists all available genres'

    @staticmethod
    def handle(*args):
        print 'genres command called'


class Play(Command):
    name = 'play'
    pattern = 'play {o}'
    example = ('play chillout', 'play username/playlist',)
    description = 'Use this command to play genres and resume paused track'

    @staticmethod
    def handle(*args):
        print 'play command called'


class Quit(Command):
    name = 'quit'
    pattern = 'quit'
    example = ('quit',)
    description = 'Close cmd.fm and turn off music'

    @staticmethod
    def handle(*args):
        sys.exit()
