# -*- coding: utf-8 -*-

import os
import yaml
import logging
import importlib
import importlib.util
from mumbleroni.core.module.abstract_module import AbstractModule
from mumbleroni.core.module.datastructure import Manifest
from mumbleroni.core.module.constants import MANIFEST_FILE_NAME

_logger = logging.getLogger(__name__)


class ModuleLoader:
    MODULE_PACKAGE_NAME_SCAFFOLD = "mumbleroni.modules.{}"

    def __init__(self, mumble, command_manager):
        self._mumble = mumble
        self._command_manager = command_manager
        self._load_all_modules()

    def _load_all_modules(self):
        for dirpath, dirnames, filenames in os.walk(r"C:\dev\python\MumbleRoni\mumbleroni\modules"):
            if MANIFEST_FILE_NAME in filenames:
                with open(os.path.join(dirpath, MANIFEST_FILE_NAME), "r") as f:
                    manifest = Manifest.from_dict(yaml.load(f))
                    _logger.info("Found module called: \"{}\" with the version: \"{}\"".format(manifest.name, manifest.version))

                for file in filenames:
                    if file.endswith(".py"):
                        module_name = self.MODULE_PACKAGE_NAME_SCAFFOLD.format(os.path.basename(dirpath))
                        spec = importlib.util.spec_from_file_location(module_name, os.path.join(dirpath, file))
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
            else:
                _logger.info("The module directory: {} does not contain a manifest file. So it won't be "
                             "loaded.".format(dirpath))

        modules = AbstractModule.__subclasses__()
        _logger.info(modules)

        for module in modules:
            try:
                _logger.info("Loading module named: {}".format(module.__name__))
                module(self._mumble)
                self._command_manager.command_registry.register_queued_commands()
                _logger.info("Successfully loaded the module.")
            except:
                _logger.error("An error occured while trying to load a module.", exc_info=True)
                self._command_manager.command_registry.clear_queue()
