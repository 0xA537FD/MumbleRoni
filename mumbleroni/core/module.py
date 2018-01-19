# -*- coding: utf-8 -*-

import logging

from mumbleroni.core.command.command_manager import CommandManager

_logger = logging.getLogger(__name__)


class AbstractModule:
    _register_command = CommandManager.register_command

    def __init__(self, mumble):
        self._mumble = mumble

    def _send_message_to_channel(self, message):
        self._mumble.channels[self._mumble.users.myself["channel_id"]].send_text_message(message)


class ModuleLoader:
    def __init__(self, mumble):
        self._mumble = mumble
        self._modules = []
        self._init_modules()

    def _init_modules(self):
        modules = AbstractModule.__subclasses__()

        for module in modules:
            try:
                self._modules.append(module(self._mumble))
            except Exception:
                _logger.error("An error occured while trying to load a module.", exc_info=True)
                _logger.info(self._modules)

    @property
    def modules(self):
        return self._modules
