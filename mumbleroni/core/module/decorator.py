# -*- coding: utf-8 -*-

import logging

_logger = logging.getLogger(__name__)


class Command:
    def command(self, command_name):
        def decorator(function):
            _logger.info("registering command: {}".format(command_name))

            return function
        return decorator
