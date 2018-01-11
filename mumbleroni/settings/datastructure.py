# -*- coding: utf-8 -*-

import os

from mumbleroni.datastructure import IDictParseable


class Settings(IDictParseable):
    DEFAULT_COMMAND_PREFIX = "!"

    def __init__(self):
        self._server = Server()
        self._command_prefix = self.DEFAULT_COMMAND_PREFIX

    @classmethod
    def parse_from_dict(cls, d):
        result = Settings()
        result.server = Server.parse_from_dict(d)

        return result

    def parse_to_dict(self):
        result = {}
        result[self._server.KEY_SERVER] = self._server.parse_to_dict()

        return result

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        self._server = value

    @property
    def command_prefix(self):
        return self._command_prefix

    @command_prefix.setter
    def command_prefix(self, value):
        self._command_prefix = value


class Server(IDictParseable):
    DEFAULT_MUMBLE_PORT = 64738

    KEY_SERVER = "server"
    KEY_HOST = "host"
    KEY_PORT = "port"
    KEY_USERNAME = "username"
    KEY_PASSWORD = "password"
    KEY_CERTIFICATE_PATH = "certificate_path"
    KEY_KEYFILE = "keyfile"
    KEY_RECONNECT = "reconnect"
    KEY_TOKENS = "tokens"

    def __init__(self):
        self._host = None
        self._port = self.DEFAULT_MUMBLE_PORT
        self._username = None
        self._password = None
        self._certificate_path = None
        self._keyfile = None
        self._reconnect = True
        self._tokens = []

    @classmethod
    def parse_from_dict(cls, d):
        """
        Parses a dictionary into a Server object and validates it.
        """
        result = Server()
        result.host = d[cls.KEY_SERVER].get(cls.KEY_HOST)
        result.port = d[cls.KEY_SERVER].get(cls.KEY_PORT, cls.DEFAULT_MUMBLE_PORT)
        result.username = d[cls.KEY_SERVER].get(cls.KEY_USERNAME)
        result.password = d[cls.KEY_SERVER].get(cls.KEY_PASSWORD)
        result.certificate_path = d[cls.KEY_SERVER].get(cls.KEY_CERTIFICATE_PATH)
        result.keyfile = d[cls.KEY_SERVER].get(cls.KEY_KEYFILE)
        result.reconnect = d[cls.KEY_SERVER].get(cls.KEY_RECONNECT, False)
        result.tokens = d[cls.KEY_SERVER].get(cls.KEY_TOKENS, [])
        cls.validate(result)

        return result

    def parse_to_dict(self):
        return {
            self.KEY_HOST: self._host,
            self.KEY_PORT: self._port,
            self.KEY_USERNAME: self._username,
            self.KEY_PASSWORD: self._password,
            self.KEY_CERTIFICATE_PATH: self._certificate_path,
            self.KEY_KEYFILE: self._keyfile,
            self.KEY_RECONNECT: self._reconnect,
            self.KEY_TOKENS: self.KEY_TOKENS,
        }

    @classmethod
    def validate(cls, server):
        cls._validate_host(server)
        cls._validate_port(server)
        cls._validate_username(server)
        cls._validate_certificate_path(server)
        # cls._validate_keyfile(server)
        cls._validate_reconnect(server)
        cls._validate_tokens(server)

    @classmethod
    def _validate_host(cls, server):
        if server.host is None:
            raise ValueError("Missing {}.".format(cls.KEY_HOST))
        if type(server.host) != str:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_HOST, type(server.host)))
        if server.host == "":
            raise ValueError("The {} is empty.".format(cls.KEY_HOST))

    @classmethod
    def _validate_port(cls, server):
        if server.port is None:
            raise ValueError("Missing {}.".format(cls.KEY_PORT))
        if type(server.port) != int:
            raise ValueError("The {} has an invalid type... Expected type int "
                             "got {}".format(cls.KEY_PORT, type(server.port)))

    @classmethod
    def _validate_username(cls, server):
        if server.username is None:
            raise ValueError("Missing {}.".format(cls.KEY_USERNAME))
        if type(server.username) != str:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_USERNAME, type(server.username)))
        if server.username == "":
            raise ValueError("The {} is empty.".format(cls.KEY_USERNAME))

    @classmethod
    def _validate_certificate_path(cls, server):
        if server.certificate_path is None:
            raise ValueError("Missing {}.".format(cls.KEY_CERTIFICATE_PATH))
        if type(server.certificate_path) != str:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_CERTIFICATE_PATH, type(server.certificate_path)))
        if server.certificate_path == "":
            raise ValueError("The {} is empty.".format(cls.KEY_CERTIFICATE_PATH))
        if not os.path.exists(server.certificate_path):
            raise ValueError("The path from {} does not exist.".format(cls.KEY_CERTIFICATE_PATH))

    @classmethod
    def _validate_keyfile(cls, server):
        if server.keyfile is None:
            return
        if type(server.keyfile) != str:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_KEYFILE, type(server.keyfile)))
        if server.keyfile == "":
            raise ValueError("The {} is empty.".format(cls.KEY_KEYFILE))
        if not os.path.exists(server.keyfile):
            raise ValueError("The path from {} does not exist.".format(cls.KEY_KEYFILE))

    @classmethod
    def _validate_reconnect(cls, server):
        if type(server.reconnect) != bool:
            raise ValueError("The {} has an invalid type... Expected type str "
                             "got {}".format(cls.KEY_RECONNECT, type(server.reconnect)))

    @classmethod
    def _validate_tokens(cls, server):
        if server.tokens is None or len(server.tokens) < 1:
            return
        if type(server.tokens) != list:
            raise ValueError("The {} has an invalid type... Expected type list "
                             "got {}".format(cls.KEY_TOKENS, type(server.tokens)))
        if len(server.tokens) >= 1:
            for token in server.tokens:
                if type(token) != str:
                    raise ValueError("An entry in {} had the wrong type... Expected type str "
                                     "got {}".format(cls.KEY_TOKENS, type(token)))

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, value):
        self._host = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def certificate_path(self):
        return self._certificate_path

    @certificate_path.setter
    def certificate_path(self, value):
        self._certificate_path = value

    @property
    def keyfile(self):
        return self._keyfile

    @keyfile.setter
    def keyfile(self, value):
        self._keyfile = value

    @property
    def reconnect(self):
        return self._reconnect

    @reconnect.setter
    def reconnect(self, value):
        self._reconnect = value

    @property
    def tokens(self):
        return self._tokens

    @tokens.setter
    def tokens(self, value):
        self._tokens = value
