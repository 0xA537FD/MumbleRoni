# -*- coding: utf-8 -*-


class IDictParseable:
    """
    Describes a datastructure that is parseable into and from a dict.
    """
    @classmethod
    def parse_from_dict(cls, d):
        raise NotImplementedError

    def parse_to_dict(self):
        raise NotImplementedError
