# -*- coding: utf-8 -*-

from mumbleroni.core.command.error import RegistrationError
from mumbleroni.settings.settingsparser import SettingsParser
from mumbleroni.logging import Logger


class CommandManager:
    COMMAND_SCAFFOLD = "{prefix}{command}"

    _logger = Logger(__name__).get
    _commands = {}

    def __init__(self):
        self._settings = SettingsParser.parse()

    @classmethod
    def register_command(cls, command, function):
        """
        :param command: The name of the command.
        :param func: The function it will trigger.
        """
        if command in cls._commands.keys():
            raise RegistrationError("A command with the name {} already exists.".format(command))

        cls._commands[command] = function

    def check_message_and_execute(self, message):
        """
        Check if a message is a command and execute it if it is.
        :param message: The message.
        """
        if not message.startswith(self._settings.command_prefix):
            self._logger.info("The passed message does not start with a command.")
            return
        self._logger.info("Recognised command {}".format(message.split(" ")[0]))

        for command in self._commands.keys():
            command_with_prefix = self.COMMAND_SCAFFOLD.format(prefix=self._settings.command_prefix,
                                                               command=command)
            if message.startswith(command_with_prefix):
                self._logger.info("Found function for command {}".format(command_with_prefix))
                self._commands[command].__call__(message)
