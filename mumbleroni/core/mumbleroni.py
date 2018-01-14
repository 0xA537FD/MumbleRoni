# -*- coding: utf-8 -*-

import time
import threading as th
import pymumble.pymumble_py3 as mmbl
import pymumble.pymumble_py3.callbacks as mmbl_callbacks

from mumbleroni.logging import Logger
from mumbleroni.settings.settingsparser import SettingsParser
from mumbleroni.core.command.command_manager import CommandManager
from mumbleroni.core.module import ModuleLoader


class MumbleRoni(th.Thread):
    _logger = Logger(__name__).get

    def __init__(self):
        th.Thread.__init__(self)
        self._settings = SettingsParser.parse()
        self._command_manager = CommandManager()
        self._main_thread = None
        self._logger.debug("Credentials which will be used to connect to the server: {}"
                           .format(self._settings.server.parse_to_dict()))
        self._mumble = mmbl.Mumble(host=self._settings.server.host,
                                   user=self._settings.server.username,
                                   port=self._settings.server.port,
                                   password=self._settings.server.password,
                                   certfile=self._settings.server.certificate_path,
                                   keyfile=self._settings.server.keyfile,
                                   reconnect=self._settings.server.reconnect,
                                   tokens=self._settings.server.tokens,
                                   debug=False)
        self._module_loader = ModuleLoader(self._mumble)
        self._init_callbacks()
        self._mumble.set_codec_profile("audio")

    def _init_callbacks(self):
        self._mumble.callbacks.set_callback(mmbl_callbacks.PYMUMBLE_CLBK_TEXTMESSAGERECEIVED,
                                            self._text_message_received)

    def run(self):
        self._logger.info("Connecting to the server.")
        self._mumble.start()
        self._mumble.is_ready()
        self._connect_to_default_channel()
        self._logger.info("Connected to the server.")
        self._main_thread = th.Thread(target=self._start_main_thread)
        self._main_thread.start()
        self._main_thread.join()
        super(MumbleRoni, self).run()

    def _connect_to_default_channel(self):
        if self._settings.server.default_channel is None:
            self._logger.info("No default channel was passed so the bot will connect to the root channel.")
            return

        if type(self._settings.server.default_channel) == int:
            self._logger.info("The following channel id was passed: {}".format(self._settings.server.default_channel))
            self._mumble.channels[self._settings.server.default_channel].move_in()
        else:
            self._logger.info("The following channel name was passed: {}".format(self._settings.server.default_channel))
            self._mumble.channels.find_by_name(self._settings.server.default_channel).move_in()

    def _start_main_thread(self):
        while True:
            time.sleep(1)

    def _text_message_received(self, text):
        message = text.message
        self._logger.info("Message: {}".format(message))
        self._command_manager.check_message_and_execute(message)

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value
