# -*- coding: utf-8 -*-


class Playlist:
    def __init__(self):
        self._content = []
        self._currently_playing = None

    def is_empty(self):
        return len(self._content) < 1 and self._currently_playing is None

    def add_song(self, song):
        song.id = self._get_last_song_id() + 1
        self._content.append(song)

    def _get_last_song_id(self):
        if len(self._content) < 1:
            return 0
        else:
            return self._content[len(self._content) - 1].id

    @property
    def currently_playing(self):
        return self._currently_playing

    @currently_playing.setter
    def currently_playing(self, value):
        self._currently_playing = value


class Song:
    def __init__(self):
        self._id = 0
        self._title = None
        self._url = None
        self._is_playing = False

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def is_playing(self):
        return self._is_playing

    @is_playing.setter
    def is_playing(self, value):
        self._is_playing = value
