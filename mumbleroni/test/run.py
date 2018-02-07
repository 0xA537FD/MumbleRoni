# -*- coding: utf-8 -*-

import os
import unittest
from mumbleroni.settings.datastructure import Settings


class SettingsDataStructureTests(unittest.TestCase):
    def setUp(self):
        self._host = "example.domain.com"
        self._port = 1337
        self._user = "MumbleRoni"
        self._password = "123456"
        self._default_channel_str = "In - Game"
        self._default_channel_int = 1
        self._certificate_path = os.path.curdir

    def test_parse_from_none(self):
        with self.assertRaises(ValueError):
            Settings.from_dict(None)

    def test_parse_from_empty_dict(self):
        with self.assertRaises(ValueError):
            Settings.from_dict({})

    def test_parse_from_dict_missing_host(self):
        settings = {
            "server": {
                "username": self._host,
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_empty_host(self):
        settings = {
            "server": {
                "host": "",
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_host_wrong_type(self):
        settings = {
            "server": {
                "host": 123,
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_missing_username(self):
        settings = {
            "server": {
                "host": self._host,
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_empty_username(self):
        settings = {
            "server": {
                "host": self._host,
                "username": "",
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_username_wrong_type(self):
        settings = {
            "server": {
                "host": self._host,
                "username": 123,
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_empty_password(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "password": ""
            }
        }

        expected = Settings()
        expected.server.host = self._host
        expected.server.username = self._user
        expected.server.password = ""

        actual = Settings.from_dict(settings)

        assert expected.server.host == actual.server.host
        assert expected.server.username == actual.server.username
        assert expected.server.password == actual.server.password

    def test_parse_from_dict_password_wrong_type(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "password": 123
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_default_channel_wrong_type(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "default_channel": False,
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_default_channel_str(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "default_channel": self._default_channel_str,
            }
        }

        expected = Settings()
        expected.server.host = self._host
        expected.server.username = self._user
        expected.server.default_channel = self._default_channel_str

        actual = Settings.from_dict(settings)

        assert expected.server.host == actual.server.host
        assert expected.server.username == actual.server.username
        assert expected.server.default_channel == actual.server.default_channel

    def test_parse_from_dict_default_channel_int(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "default_channel": self._default_channel_int,
            }
        }

        expected = Settings()
        expected.server.host = self._host
        expected.server.username = self._user
        expected.server.default_channel = self._default_channel_int

        actual = Settings.from_dict(settings)

        assert expected.server.host == actual.server.host
        assert expected.server.username == actual.server.username
        assert expected.server.default_channel == actual.server.default_channel

    def test_parse_from_dict_port_wrong_type(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "port": "some_port",
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_port_is_none(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "port": None,
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_port(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "port": self._port,
            }
        }

        expected = Settings()
        expected.server.host = self._host
        expected.server.username = self._user
        expected.server.port = self._port

        actual = Settings.from_dict(settings)

        assert expected.server.host == actual.server.host
        assert expected.server.username == actual.server.username
        assert expected.server.port == actual.server.port

    def test_parse_from_dict_certificate_path_wrong_type(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "certificate_path": 123,
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_certificate_path_invalid_path(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "certificate_path": "invalid",
            }
        }

        with self.assertRaises(ValueError):
            Settings.from_dict(settings)

    def test_parse_from_dict_certificate_path_cur_dir(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
                "certificate_path": self._certificate_path,
            }
        }

        expected = Settings()
        expected.server.host = self._host
        expected.server.username = self._user
        expected.server.certificate_path = self._certificate_path

        actual = Settings.from_dict(settings)

        assert expected.server.host == actual.server.host
        assert expected.server.username == actual.server.username
        assert expected.server.certificate_path == actual.server.certificate_path

    def test_parse_from_valid_dict_1(self):
        settings = {
            "server": {
                "host": self._host,
                "username": self._user,
            }
        }
        expected = Settings()
        expected.server.host = self._host
        expected.server.username = self._user

        actual = Settings.from_dict(settings)

        assert actual.server.host is expected.server.host
        assert actual.server.username is expected.server.username


if __name__ == '__main__':
    unittest.main()
