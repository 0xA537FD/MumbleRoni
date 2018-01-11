# -*- coding: utf-8 -*-

import os
import logging

LOG_DIR_NAME = "log"

LOG_LEVEL_DEBUG = "debug"
LOG_LEVEL_INFO = "info"
LOG_LEVEL_WARNING = "warning"
LOG_LEVEL_ERROR = "error"
LOG_LEVEL_CRITICAL = "critical"

LOG_LEVEL_TO_LOGGING_MAPPING = {
    LOG_LEVEL_DEBUG: logging.DEBUG,
    LOG_LEVEL_INFO: logging.INFO,
    LOG_LEVEL_WARNING: logging.WARNING,
    LOG_LEVEL_ERROR: logging.ERROR,
    LOG_LEVEL_CRITICAL: logging.CRITICAL,
}

LOGGING_TO_LOG_LEVEL_MAPPING = {
    logging.DEBUG: LOG_LEVEL_DEBUG,
    logging.INFO: LOG_LEVEL_INFO,
    logging.WARNING: LOG_LEVEL_WARNING,
    logging.ERROR: LOG_LEVEL_ERROR,
    logging.CRITICAL: LOG_LEVEL_CRITICAL,
}


class Logger:
    """
    Base *Logger* class for mumbleroni. Loggers should be constructed with this class.
    **Example**:
    _logger = Logger(__name__).get
    """
    log_level = logging.INFO

    def __init__(self, name):
        name = name.replace(".log", "")
        logger = logging.getLogger("mumbleroni.%s" % name)

        if type(self.log_level) == int:
            self._log_level = self.log_level
        else:
            self._log_level = self.convert_internal_log_level_to_logging_log_level(self.log_level)

        logger.setLevel(self._log_level)

        if not logger.handlers:
            file_name = os.path.join(os.path.join(os.path.abspath(os.path.curdir), LOG_DIR_NAME), "mumbleroni.log")
            file_handler = logging.FileHandler(file_name)
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s >> %(message)s")
            file_handler.setFormatter(formatter)
            file_handler.setLevel(self._log_level)
            logger.addHandler(file_handler)
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            stream_handler.setLevel(self._log_level)
            logger.addHandler(stream_handler)

        self._logger = logger

    @classmethod
    def convert_internal_log_level_to_logging_log_level(cls, internal_log_level):
        return LOG_LEVEL_TO_LOGGING_MAPPING[internal_log_level.upper()]

    @classmethod
    def convert_logging_log_level_to_internal_log_level(cls, logging_log_level):
        return LOGGING_TO_LOG_LEVEL_MAPPING[logging_log_level]

    @property
    def get(self):
        return self._logger
