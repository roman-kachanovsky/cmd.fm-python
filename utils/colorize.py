from __future__ import unicode_literals


class Colors(object):
    ENDC = 0

    LIME = 36
    GRAY = 90
    RED = 91
    GREEN = 92
    YELLOW = 93
    BLUE = 94
    PURPLE = 95
    LBLUE = 96
    BLACK = 97


def colorize(color, text):
    return '\033[{}m{}\033[{}m'.format(color, text, Colors.ENDC)
