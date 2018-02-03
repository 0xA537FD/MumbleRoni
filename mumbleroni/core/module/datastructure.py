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
        if manifest.name is None:
            raise ValueError("Missing {}".format(cls.KEY_NAME))
        if type(manifest.name) != str:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_NAME, type(manifest.name)))
        if manifest.name is "":
            raise ValueError("The {} is empty.".format(cls.KEY_NAME))

    @classmethod
    def _validate_version(cls, manifest):
        if manifest.version is None:
            raise ValueError("Missing {}".format(cls.KEY_VERSION))
        if type(manifest.version) != str:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_VERSION, type(manifest.version)))
        if manifest.version is "":
            raise ValueError("The {} is empty.".format(cls.KEY_VERSION))

    @classmethod
    def _validate_summary(cls, manifest):
        if manifest.summary is None:
            return
        if type(manifest.summary) != str:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_SUMMARY, type(manifest.summary)))
        if manifest.summary is "":
            raise ValueError("The {} is empty.".format(cls.KEY_SUMMARY))

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
