from __future__ import unicode_literals, absolute_import

import sys
import unittest
import mock
import re

from fm import Fm

from .mock_client import MockClient


class TestFm(unittest.TestCase):

    def setUp(self):
        self.mock_stdin = mock.create_autospec(sys.stdin)
        self.mock_stdout = mock.create_autospec(sys.stdout)
        self.mock_client = MockClient('test_key')

    def create(self):
        return Fm(stdin=self.mock_stdin, stdout=self.mock_stdout, client=self.mock_client, test=True)

    @staticmethod
    def clear_coloring(text):
        return re.sub(r'\033\[[0-9]{1,2}m', '', text)

    def cli_response(self):
        return self.clear_coloring(self.mock_stdout.write.call_args_list[0][0][0])

    def test_wrong_command(self):
        cli = self.create()
        self.assertFalse(cli.onecmd('wrong_command'))
        self.assertEqual(self.cli_response(), '    Unknown command wrong_command\n')
        self.mock_stdout.reset_mock()

    def test_genres(self):
        cli = self.create()
        self.assertFalse(cli.onecmd('genres'))
        cli_response = self.cli_response()
        self.assertTrue('- GENRES -' in cli_response)  # First line
        self.assertTrue('R - Rock' in cli_response)  # Genre
        self.assertTrue('play {genre}' in cli_response)  # Last line
        self.mock_stdout.reset_mock()

    # def test_play(self):
    #     cli = self.create()
    #     self.assertFalse(cli.onecmd('play'))
    #     self.assertEqual(self.cli_response(), 'debug: play/p command output\n')
    #     self.mock_stdout.reset_mock()
    #     self.assertFalse(cli.onecmd('p'))
    #     self.assertEqual(self.cli_response(), 'debug: play/p command output\n')
    #     self.mock_stdout.reset_mock()

    def test_quit(self):
        cli = self.create()
        with self.assertRaises(SystemExit):
            cli.onecmd('quit')
        with self.assertRaises(SystemExit):
            cli.onecmd('q')


if __name__ == '__main__':
    unittest.main()
