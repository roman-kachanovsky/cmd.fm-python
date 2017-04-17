from __future__ import unicode_literals

import re


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

    HMAP = {
        'e': ENDC,
        'l': LIME,
        'g': GRAY,
        'gn': GREEN,
        'r': RED,
        'y': YELLOW,
        'b': BLUE,
        'p': PURPLE,
        'lb': LBLUE,
        'bk': BLACK
    }


def colorize(color, text):
    return '\033[{}m{}\033[{}m'.format(color, text, Colors.ENDC)


def render(template):
    pattern = '(?i)({{(e-)?[a-z]{1}}})'
    matches = [m[0].replace('{{', '').replace('}}', '') for m in re.findall(pattern, template)]
    rendered_text = template

    for match in matches:
        if 'e-' in match:
            color = Colors.HMAP.get(match.replace('e-', ''))
        else:
            color = Colors.HMAP.get(match)

        if color is not None:
            if 'e-' in match:
                rendered_color = '\033[0m\033[{}m'.format(color)
            else:
                rendered_color = '\033[{}m'.format(color)

            rendered_text = rendered_text.replace('{{' + match + '}}', rendered_color)
        else:
            raise ValueError('Unexpected tag: {}'.format('{{' + match + '}}'))

    return rendered_text
