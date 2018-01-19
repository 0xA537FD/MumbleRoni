# -*- coding: utf-8 -*-

import os
import yaml
import logging

from mumbleroni.settings.datastructure import Settings, Server
from mumbleroni.settings.constants import CONFIG_FOLDER_NAME, CONFIG_FILE_NAME

_logger = logging.getLogger(__name__)


class SettingsParser:
    @classmethod
    def parse(cls):
        """
        Parse the settings file into an object.
        :return: A :see Settings: object with the corresponding data.
        """
        _logger.info("Parsing settings")
        with open(os.path.join(os.path.join(os.path.abspath(os.path.curdir), CONFIG_FOLDER_NAME), CONFIG_FILE_NAME), "r") as f:
            settings_yaml = yaml.load(f)
            _logger.debug("Settings object raw: {}".format(settings_yaml))
            _logger.info("Finished parsing settings.")

            return Settings.parse_from_dict(settings_yaml)
