from __future__ import unicode_literals

import requests
import string
from contextlib import closing
from random import shuffle


class DirbleClient(object):
    DOMAIN = 'http://api.dirble.com/v2'
    GENRES = '/categories/{}'
    STATIONS = '/category/{}/stations'

    genres = None
    current_category_id = None
    current_stations = None
    active_station = None

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

    def get_stations(self):
        response = requests.get(self.build_request_uri(self.STATIONS, self.current_category_id))

        if response.ok:
            return response.json()
        return []

    def search_genre(self, genre_name):
        for genre in sorted(self.genres, key=lambda x: (len(x.get('title', '')), x.get('title', ''))):
            if genre_name.lower() in genre.get('title', '').lower():
                return genre
        return None

    def update_active_station(self, category_id):
        self.active_station = None
        self.current_category_id = category_id

        if not self.current_stations:
            # Keep list of current genre stations in memory to prevent excess requests
            self.current_stations = self.get_stations()

        if not self.current_stations:
            return None

        shuffle(self.current_stations)  # Increase our chances to take more varied streams

        for station in self.current_stations:
            stream_url = station['streams'][0].get('stream', '') if len(station.get('streams', [])) else ''
            if not stream_url:
                continue

            try:
                with closing(requests.get(stream_url, stream=True)) as r:
                    if r.ok:  # Take the first "in air" stream
                        self.active_station = station
                        break
            except requests.exceptions.ConnectionError:
                continue

        return self.active_station

    @property
    def stream_url(self):
        return self.active_station['streams'][0].get('stream', '') \
            if self.active_station and len(self.active_station.get('streams', [])) else ''

    def get_stream(self, category_id, renew_active_station=False):
        if not self.active_station or self.current_category_id != category_id or renew_active_station:
            return self.stream_url if self.update_active_station(category_id) else ''
        return self.stream_url
