# -*- coding: utf-8 -*-

from mumbleroni.core.command.manager import CommandRegistry


class AbstractModule:
    _register_command = CommandRegistry.add_to_queue

    def __init__(self, mumble):
        self._mumble = mumble

    def _send_message_to_channel(self, message):
        self._mumble.channels[self._mumble.users.myself["channel_id"]].send_text_message(message)
