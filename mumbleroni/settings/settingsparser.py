# -*- coding: utf-8 -*-

import os
import yaml

from mumbleroni.logging import Logger
from mumbleroni.settings.datastructure import Settings, Server
from mumbleroni.settings.util import CONFIG_FOLDER_NAME, CONFIG_FILE_NAME


class SettingsParser:
    _logger = Logger(__name__).get

    @classmethod
    def parse(cls):
        """
        Parse the settings file into an object.
        :return: A :see Settings: object with the corresponding data.
        """
        cls._logger.info("Parsing settings")
        with open(os.path.join(os.path.join(os.path.abspath(os.path.curdir), CONFIG_FOLDER_NAME), CONFIG_FILE_NAME), "r") as f:
            settings_yaml = yaml.load(f)
            cls._logger.debug("Settings object raw: {}".format(settings_yaml))

            return Settings.parse_from_dict(settings_yaml)
