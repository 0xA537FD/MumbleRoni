# -*- coding: utf-8 -*-

import inspect
import logging

from mumbleroni.settings.settingsparser import SettingsParser
from mumbleroni.core.command.registry import CommandRegistry
from mumbleroni.core.command.constants import COMMAND_SCAFFOLD

_logger = logging.getLogger(__name__)


class CommandManager:
    def __init__(self):
        self._settings = SettingsParser.parse()
        self._command_registry = CommandRegistry()

    def check_and_execute_message(self, message):
        """
        Check if a message is a command and execute it.
        :param message: The message that should be checked and executed.
        """
        if not message.startswith(self._settings.command_prefix):
            _logger.info("The passed message does not start with the command prefix.")
            return
        _logger.info("Recognised command {}".format(message.split(" ")[0]))

        for command in self._command_registry.commands.keys():
            command_with_prefix = COMMAND_SCAFFOLD.format(prefix=self._settings.command_prefix,
                                                          command=command)
            if message.startswith(command_with_prefix):
                _logger.info("Found function for command {}".format(command_with_prefix))

                func_args = inspect.getfullargspec(self._command_registry.commands[command])
                if len(func_args.args) > 1:
                    self._command_registry.commands[command].__call__(message)
                else:
                    self._command_registry.commands[command].__call__()

    @property
    def command_registry(self):
        return self._command_registry
