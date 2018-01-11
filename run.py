# -*- coding: utf-8 -*-

import sys

from optparse import OptionParser
from mumbleroni.core import MumbleRoni

VERSION_FILE_NAME = "version"


def main():
    mumbleroni = MumbleRoni()
    mumbleroni.run()


def get_option_parser():
    parser = OptionParser(usage="Usage: %prog [options]", version=get_program_version())
    parser.add_option("--create-tables", dest="create_tables", action="store_true", default=False,
                      help="Create the database tables.")
    # parser.add_option("--log-level", dest="log_level", help="Set the log level for mumbleroni. Possible values: DEBUG, "
                      # "INFO, WARNING, ERROR, CRITICAL (The value is case insensitive.)")

    return parser


def get_program_version():
    with open(VERSION_FILE_NAME, "r") as f:
        lines = f.readlines()

        if len(lines) >= 1:
            return lines[0]

    return "Unknown version"


if __name__ == '__main__':
    raw_argv = sys.argv

    parser = get_option_parser()
    options, args = parser.parse_args()

    # if options.log_level is not None:
        # Logger.log_level = options.log_level

    main()


