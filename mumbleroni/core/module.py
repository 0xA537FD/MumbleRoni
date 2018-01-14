# -*- coding: utf-8 -*-

from mumbleroni.core.command.command_manager import CommandManager
from mumbleroni.logging import Logger


class AbstractModule:
    def __init__(self, mumble):
        self._mumble = mumble

    def _register_command(self, command_name, function):
        CommandManager.register_command(command_name, function)

    def _send_message_to_channel(self, message):
        self._mumble.channels[self._mumble.users.myself["channel_id"]].send_text_message(message)


class ModuleLoader:
    _logger = Logger(__name__).get

    def __init__(self, mumble):
        self._mumble = mumble
        self._modules = []
        self._init_modules()

    def _init_modules(self):
        modules = AbstractModule.__subclasses__()

        for module in modules:
            self._modules.append(module(self._mumble))
