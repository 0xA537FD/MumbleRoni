# -*- coding: utf-8 -*-

import logging
from mumbleroni.core.module.abstract_module import AbstractModule

_logger = logging.getLogger(__name__)


class ModuleLoader:
    def __init__(self, mumble, command_manager):
        self._mumble = mumble
        self._command_manager = command_manager
        self._modules = []
        self._init_modules()

    def _init_modules(self):
        modules = AbstractModule.__subclasses__()

        for module in modules:
            try:
                _logger.info("Loading module named: {}".format(module.__name__))
                self._modules.append(module(self._mumble))
                self._command_manager.command_registry.register_queued_commands()
                _logger.info("Successfully loaded the module.")
            except Exception:
                _logger.error("An error occured while trying to load a module.", exc_info=True)
                self._command_manager.command_registry.clear_queue()

    @property
    def modules(self):
        return self._modules
