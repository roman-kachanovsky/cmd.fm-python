from __future__ import unicode_literals

import requests


class DirbleClient(object):
    DOMAIN = 'http://api.dirble.com/v2'
    GENRES = '/categories/{}'
    STATIONS = '/categories/{}/stations'

    genres = None

    def __init__(self, api_key):
        self.api_key = api_key
        self.genres = self.get_genres()

    @property
    def token(self):
        return '?token={}'.format(self.api_key)

    def build_request_uri(self, endpoint, arg=''):
        return self.DOMAIN + endpoint.format(arg) + self.token

    def get_genres(self):
        response = requests.get(self.build_request_uri(self.GENRES))

        if response.ok:
            return response.json()
        return []

    def get_stations(self, category_id):
        response = requests.get(self.build_request_uri(self.STATIONS, category_id))

        if response.ok:
            return response.json()
        return []

    def search_genre(self, genre_name):
        for genre in self.genres:
            if genre_name.lower() == genre.get('title', '').lower():
                return genre.get('id', 0)
        return 0
