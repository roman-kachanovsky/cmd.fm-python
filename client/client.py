from __future__ import unicode_literals

import requests
import string


class DirbleClient(object):
    DOMAIN = 'http://api.dirble.com/v2'
    GENRES = '/categories/{}'
    STATIONS = '/categories/{}/stations'

    genres = None

    def __init__(self, api_key):
        self.api_key = api_key
        self.genres = self.get_genres()

    @property
    def _uri_token(self):
        return '?token={}'.format(self.api_key)

    def build_request_uri(self, endpoint, arg=''):
        return self.DOMAIN + endpoint.format(arg) + self._uri_token

    def get_genres(self):
        response = requests.get(self.build_request_uri(self.GENRES))

        if response.ok:
            return response.json()
        return []

    @property
    def genres_titles(self):
        titles = dict()

        for title in sorted([g.get('title', '') for g in self.genres]):
            first_letter = title[0].upper()
            if title[0] in string.digits:
                first_letter = '#'
            titles[first_letter] = titles.get(first_letter, list()) + [title]

        return titles

    def get_stations(self, category_id):
        response = requests.get(self.build_request_uri(self.STATIONS, category_id))

        if response.ok:
            return response.json()
        return []

    def search_genre(self, genre_name):
        for genre in sorted(self.genres, key=lambda x: (len(x.get('title', '')), x.get('title', ''))):
            if genre_name.lower() in genre.get('title', '').lower():
                return genre.get('id')
        return None
