# -*- coding: utf-8 -*-

import time
import pafy
import audioop
import logging
import threading as th
import subprocess as sp

from mumbleroni.core.module.abstract_module import AbstractModule
from pymumble.pymumble_py3 import Mumble
from bs4 import BeautifulSoup

_logger = logging.getLogger(__name__)


class YoutubeMusicPlayerModule(AbstractModule):
    def __init__(self, mumble: Mumble):
        super(YoutubeMusicPlayerModule, self).__init__()
        self._mumble = mumble
        self._ffmpeg_thread = None
        self._music_thread = None
        self._stop_music = False
        self._video = None
        self._register_commands()

    def _register_commands(self):
        self._register_command("play", self.play)
        self._register_command("stop", self.stop)
        self._register_command("info", self.info)

    def play(self, message):
        self._stop_music = False
        music_url = None

        try:
            soup = BeautifulSoup(message, "html.parser")
            music_url = soup.find("a").get("href")
        except:
            _logger.error("An error occurred while trying to parse the link out of the message.", exc_info=True)
            self._send_message_to_channel("An invalid link was passed with the command.")
            return

        try:
            self._video = pafy.new(music_url)
            audio_url = self._video.getbestaudio().url
            self.info()
        except:
            self._send_message_to_channel("An error occurred while trying to get the audio.")
            _logger.error("An error occurred while trying to get the audio of the video url {}".format(music_url),
                          exc_info=True)
            return

        command = ["ffmpeg", "-nostdin", "-i", audio_url, "-ac", "1", "-f", "s16le", "-ar", "48000", "-"]
        self._ffmpeg_thread = sp.Popen(command, stdout=sp.PIPE, bufsize=480)
        self._music_thread = th.Thread(target=self._play_music)
        self._music_thread.start()
        self._music_thread.join()

    def _play_music(self):
        while not self._stop_music and self._mumble.is_alive():
            out = self._ffmpeg_thread.stdout.read(480)
            if out:
                self._mumble.sound_output.add_sound(audioop.mul(out, 2, 0.1))
            else:
                time.sleep(0.01)

    def stop(self):
        self._stop_music = True
        self._mumble.sound_output.clear_buffer()
        self._video = None

        if self._ffmpeg_thread:
            self._ffmpeg_thread.kill()
            self._ffmpeg_thread = None

        if self._music_thread:
            self._music_thread.kill()
            self._music_thread = None

    def info(self):
        if self._video:
            self._send_message_to_channel("Now playing >> {title}".format(title=self._video.title))
        else:
            self._send_message_to_channel("Currently no audio is playing.")

    def _send_message_to_channel(self, message):
        self._mumble.channels[self._mumble.users.myself["channel_id"]].send_text_message(message)
