# -*- coding: utf-8 -*-


class IDictParseable:
    """
    Describes a datastructure that is parseable into and from a dict.
    """
    @classmethod
    def from_dict(cls, d):
        raise NotImplementedError

    def to_dict(self):
        raise NotImplementedError
