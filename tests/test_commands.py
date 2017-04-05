from __future__ import unicode_literals, absolute_import

import sys
import unittest
import mock

from fm import Fm


class TestFm(unittest.TestCase):

    def setUp(self):
        self.mock_stdin = mock.create_autospec(sys.stdin)
        self.mock_stdout = mock.create_autospec(sys.stdout)

    def create(self):
        return Fm(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_response(self, number_of_lines=None):
        if number_of_lines is None:
            return self.mock_stdout.write.call_args_list[0][0][0]
        return ''.join(map(lambda c: c[0][0][0], self.mock_stdout.write.call_args_list[-number_of_lines:]))

    def test_play(self):
        cli = self.create()
        self.assertFalse(cli.onecmd('play'))
        self.assertEqual(self._last_response(), 'debug: play/p command output\n')
        self.mock_stdout.reset_mock()
        self.assertFalse(cli.onecmd('p'))
        self.assertEqual(self._last_response(), 'debug: play/p command output\n')
        self.mock_stdout.reset_mock()


if __name__ == '__main__':
    unittest.main()
