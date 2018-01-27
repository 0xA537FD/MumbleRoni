# -*- coding: utf-8 -*-

import unittest


class ModuleTest(unittest.TestCase):
    def load_invalid_module(self):
        assert(1 == 1)
