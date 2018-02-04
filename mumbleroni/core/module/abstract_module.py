# -*- coding: utf-8 -*-

from mumbleroni.core.command.manager import CommandRegistry


class AbstractModule:
    _register_command = CommandRegistry.add_to_queue
