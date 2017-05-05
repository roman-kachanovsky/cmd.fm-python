from __future__ import unicode_literals

import unittest

from .mock_client import MockClient


class TestFm(unittest.TestCase):
    def setUp(self):
        self.client = MockClient('test_key')

    def test_get_genres(self):
        self.assertTrue(bool(self.client.get_genres()))
        self.assertIsInstance(self.client.get_genres(), list)

    def test_genres_titles(self):
        self.assertEqual(self.client.genres_titles,
                         {
                             'T': ['Trance', ],
                             'R': ['Rock', ],
                             'D': ['Dance', 'Dancehall'],
                         })

    def test_search_genre(self):
        self.assertEqual(self.client.search_genre('rock'), 2)
        self.assertEqual(self.client.search_genre('dancehall'), 4)
        self.assertEqual(self.client.search_genre('wrong_genre'), None)
        self.assertEqual(self.client.search_genre('ock'), 2)  # Partial search
        self.assertEqual(self.client.search_genre('ance'), 3)  # Partial search in sorted data


if __name__ == '__main__':
    unittest.main()
