from __future__ import unicode_literals, absolute_import

import unittest

from utils.colorize import colorize, Colors


class TestColorize(unittest.TestCase):
    def test_colorize(self):
        self.assertEqual(colorize(Colors.YELLOW, 'test'), '\033[93mtest\033[0m')
        self.assertEqual(colorize(Colors.GRAY, 'test'), '\033[90mtest\033[0m')
        self.assertEqual(colorize(Colors.PURPLE, 'test'), '\033[95mtest\033[0m')
        self.assertEqual(colorize(Colors.RED, 'test'), '\033[91mtest\033[0m')

    def test_render(self):
        # TODO: Test 'render' function
        pass


if __name__ == '__main__':
    unittest.main()
