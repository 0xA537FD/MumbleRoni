# -*- coding: utf-8 -*-

import time
import threading as th
from mumbleroni.core.command.manager import CommandRegistry


class AbstractModule:
    _register_command = CommandRegistry.add_to_queue
