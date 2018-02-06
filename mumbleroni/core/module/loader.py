# -*- coding: utf-8 -*-

import os
import yaml
import inspect
import logging
import importlib
import importlib.util
from mumbleroni.core.module.abstract_module import AbstractModule
from mumbleroni.core.module.datastructure import Manifest
from mumbleroni.core.module.constants import MANIFEST_FILE_NAME
from pymumble.pymumble_py3 import Mumble

_logger = logging.getLogger(__name__)


class ModuleLoader:
    PARENT_MODULE_NAME = "mumbleroni.modules"

    def __init__(self, mumble, command_manager):
        self._mumble = mumble
        self._command_manager = command_manager
        self._loaded_modules = {}
        self._modules_path = os.path.join(os.path.join(os.path.abspath(os.path.curdir), "mumbleroni"), "modules")

    def load_all_modules(self):
        self._search_modules()

    def _search_modules(self):
        for dir_path, dir_names, file_names in os.walk(self._modules_path):
            if MANIFEST_FILE_NAME in file_names:
                _logger.info("Found module in directory: {}".format(dir_path))

                manifest = self._load_module_manifest(dir_path)
                if not manifest.is_empty():
                    for file in file_names:
                        if file.endswith(".py"):
                            spec = importlib.util.spec_from_file_location(self.PARENT_MODULE_NAME,
                                                                          os.path.join(dir_path, file))
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)
                            module_classes = inspect.getmembers(module, predicate=self._is_module_class)

                            if len(module_classes) < 2:
                                _logger.error("The file: {} did not define any module class."\
                                              .format(os.path.join(dir_path, file)))
                            elif len(module_classes) == 2:
                                self._instantiate_module(manifest, module_classes[1][1])
                            elif len(module_classes) > 2:
                                _logger.error("The file: {} had too many module classes."\
                                              .format(os.path.join(dir_path, file)))
            else:
                _logger.info("The module directory: {} does not contain a manifest file. So it won't be "
                             "loaded.".format(dir_path))

    def _is_module_class(self, object):
        return inspect.isclass(object) and issubclass(object, AbstractModule)

    def _load_module_manifest(self, module_path):
        result = Manifest()

        with open(os.path.join(module_path, MANIFEST_FILE_NAME), "r") as f:
            try:
                result = Manifest.from_dict(yaml.load(f))
                _logger.info("Found module called: \"{}\" with the version: \"{}\"".format(result.name,
                                                                                           result.version))
            except ValueError:
                _logger.error("Error while loading manifest.", exc_info=True)

        return result

    def _instantiate_module(self, manifest, clazz):
        try:
            _logger.info("Loading module named: {}".format(clazz.__name__))

            module_args = inspect.getfullargspec(clazz)
            if len(module_args.args) > 1:
                for i, arg in enumerate(module_args.args):
                    if i != 0:
                        if module_args.annotations:
                            if arg in module_args.annotations.keys():
                                arg_class = module_args.annotations[arg]

                                if arg_class is Mumble:
                                    self._loaded_modules[manifest] = clazz(self._mumble)
                                else:
                                    _logger.info("The parameter {} has an unknown type {}".format(arg, arg_class))
                            else:
                                _logger.info("The parameter for the module {} has no type defined so the module "
                                             "could not be loaded.".format(clazz.__name__))
                        else:
                            _logger.info("The parameter for the module {} has no type defined so the module could "
                                         "not be loaded.".format(clazz.__name__))
            else:
                self._loaded_modules[manifest] = clazz()

            self._command_manager.command_registry.register_queued_commands()
            _logger.info("Successfully loaded the module.")
        except:
            _logger.error("An error occurred while trying to load a module.", exc_info=True)
            self._command_manager.command_registry.clear_queue()

    @property
    def loaded_modules(self):
        return self._loaded_modules
