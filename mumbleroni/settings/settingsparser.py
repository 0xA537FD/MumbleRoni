# -*- coding: utf-8 -*-

import os
import sys
import yaml
import logging

from mumbleroni.settings.datastructure import Settings, Server
from mumbleroni.settings.constants import CONFIG_DIR_NAME, CONFIG_FILE_NAME

_logger = logging.getLogger(__name__)


class SettingsParser:
    @classmethod
    def parse(cls):
        """
        Parse the settings file into an object.
        :return: A :see Settings: object with the corresponding data.
        """
        _logger.info("Parsing settings")
        config_file_path = os.path.join(CONFIG_DIR_NAME, CONFIG_FILE_NAME)

        if not os.path.exists(config_file_path):
            _logger.error("Missing configuration file: {}".format(config_file_path))
            sys.exit(1)

        with open(config_file_path, "r") as f:
            settings_yaml = yaml.load(f)
            _logger.debug("Settings object raw: {}".format(settings_yaml))
            _logger.info("Finished parsing settings.")

            return Settings.from_dict(settings_yaml)
