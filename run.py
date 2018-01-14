# -*- coding: utf-8 -*-

from optparse import OptionParser

from mumbleroni.core.constants import VERSION_FILE_NAME
from mumbleroni.core.mumbleroni import MumbleRoni


def main():
    mumbleroni = MumbleRoni()
    mumbleroni.run()


def get_option_parser():
    parser = OptionParser(usage="Usage: %prog [options]", version=get_program_version())

    return parser


def get_program_version():
    with open(VERSION_FILE_NAME, "r") as f:
        line = f.readline()

        if line is not None and line.strip() != "":
            return line.strip()

    return "Unknown version"


if __name__ == '__main__':
    parser = get_option_parser()
    options, args = parser.parse_args()

    main()


