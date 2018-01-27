# -*- coding: utf-8 -*-

from mumbleroni.datastructure import IDictParseable


class Manifest(IDictParseable):
    KEY_NAME = "name"
    KEY_VERSION = "version"
    KEY_SUMMARY = "summary"

    def __init__(self):
        self._name = None
        self._version = None
        self._summary = None

    @classmethod
    def from_dict(cls, d):
        result = Manifest()
        result.name = d.get(cls.KEY_NAME)
        result.version = d.get(cls.KEY_VERSION)
        result.summary = d.get(cls.KEY_SUMMARY)
        cls.validate(result)

        return result

    def to_dict(self):
        return {
            self.KEY_NAME: self._name,
            self.KEY_VERSION: self._version,
            self.KEY_SUMMARY: self._summary,
        }

    @classmethod
    def validate(cls, manifest):
        cls._validate_name(manifest)
        cls._validate_version(manifest)
        cls._validate_summary(manifest)

    @classmethod
    def _validate_name(cls, manifest):
        pass

    @classmethod
    def _validate_version(cls, manifest):
        pass

    @classmethod
    def _validate_summary(cls, manifest):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value
