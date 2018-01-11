# -*- coding: utf-8 -*-


class IDictParseable:
    @classmethod
    def parse_from_dict(cls, d):
        raise NotImplementedError

    def parse_to_dict(self):
        raise NotImplementedError
