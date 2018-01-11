# -*- coding: utf-8 -*-

import time
import pymumble.pymumble_py3 as mmbl
import pymumble.pymumble_py3.callbacks as mmbl_callbacks

import threading as th

from mumbleroni.logging import Logger
from mumbleroni.settings.settingsparser import SettingsParser
from mumbleroni.audio.datastructure import Playlist


class MumbleRoni:
    _logger = Logger(__name__).get

    def __init__(self):
        self._settings = SettingsParser.parse()
        self._playlist = Playlist()
        self._bot_thread = None

        self._mumble = mmbl.Mumble(host=self._settings.server.host,
                                   user=self._settings.server.username,
                                   port=self._settings.server.port,
                                   password=self._settings.server.password,
                                   certfile=self._settings.server.certificate_path,
                                   keyfile=self._settings.server.keyfile,
                                   reconnect=self._settings.server.reconnect,
                                   tokens=self._settings.server.tokens)
        self._mumble.callbacks.set_callback(mmbl_callbacks.PYMUMBLE_CLBK_TEXTMESSAGERECEIVED,
                                            self._text_message_received)
        self._mumble.start()
        self._logger.info(self._mumble.connect())

    def run(self):
        self._bot_thread = th.Thread(target=self._start_mumble_roni)
        self._bot_thread.start()
        self._bot_thread.join()

    def _start_mumble_roni(self):
        while True:
            if self._playlist.is_empty():
                pass

            time.sleep(1)

    def _text_message_received(self, message):
        self._logger.info("Message: {}".format(message))

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value
