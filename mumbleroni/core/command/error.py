# -*- coding: utf-8 -*-


class RegistrationError(Exception):
    """
    Thrown when an error occurred while.
    """
    def __init__(self, value):
        self._value = value

    def __repr__(self):
        return repr(self._value)