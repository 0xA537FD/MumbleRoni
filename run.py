# -*- coding: utf-8 -*-

import os
import sys
import yaml
import logging.config

from optparse import OptionParser
from mumbleroni.core.constants import VERSION_FILE_NAME
from mumbleroni.core.mumbleroni import MumbleRoni
from mumbleroni.constants import LOGGING_CONFIG_PATH, LOG_DIR_NAME


def main():
    mumbleroni = MumbleRoni()
    mumbleroni.start()
    mumbleroni.join()


def get_option_parser():
    parser = OptionParser(usage="Usage: %prog [options]", version=get_program_version())

    return parser


def get_program_version():
    if os.path.exists(VERSION_FILE_NAME):
        with open(VERSION_FILE_NAME, "r") as f:
            line = f.readline()

        if line is not None and line.strip() != "":
            return line.strip()

        return "Unknown version"
    else:
        print("Missing version file")
        sys.exit(1)


def setup_logging():
    if not os.path.exists(LOG_DIR_NAME):
        os.mkdir(LOG_DIR_NAME)

    if os.path.exists(LOGGING_CONFIG_PATH):
        with open(LOGGING_CONFIG_PATH, "r") as f:
            config = yaml.load(f)

        logging.config.dictConfig(config)
    else:
        print("Missing logging config")
        sys.exit(1)


if __name__ == '__main__':
    parser = get_option_parser()
    options, args = parser.parse_args()
    setup_logging()
    main()


