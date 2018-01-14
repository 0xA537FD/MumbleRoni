# -*- coding: utf-8 -*-

import time
import pafy
import audioop
import threading as th
import subprocess as sp

from mumbleroni.core.module import AbstractModule
from mumbleroni.logging import Logger
from bs4 import BeautifulSoup


class YoutubeMusicPlayerModule(AbstractModule):
    _logger = Logger(__name__).get

    def __init__(self, mumble):
        super(YoutubeMusicPlayerModule, self).__init__(mumble)
        self._ffmpeg_thread = None
        self._music_thread = None
        self._stop_music = False
        self._register_command("play", self.play)
        self._register_command("stop", self.stop)

    def play(self, message):
        self._stop_music = False
        music_link = None

        try:
            soup = BeautifulSoup(message, "html.parser")
            music_link = soup.find("a").get("href")
        except Exception:
            self._logger.error("An error occured while trying to parse the link out of the message.", exc_info=True)
            self._send_message_to_channel("No or an invalid link was passed with the command.")

        video = pafy.new(music_link)
        audio_url = video.getbestaudio().url
        self._send_message_to_channel("Now playing >>> {}".format(video.title))

        command = ["ffmpeg", "-nostdin", "-i", audio_url, "-ac", "1", "-f", "s16le", "-ar", "48000", "-"]
        self._ffmpeg_thread = sp.Popen(command, stdout=sp.PIPE, bufsize=480)
        self._music_thread = th.Thread(target=self._play_music)
        self._music_thread.start()
        self._music_thread.join()

    def stop(self, message):
        self._stop_music = True
        self._mumble.sound_output.clear_buffer()

        if self._ffmpeg_thread:
            self._ffmpeg_thread.kill()
            self._ffmpeg_thread = None

    def _play_music(self):
        while not self._stop_music and self._mumble.is_alive():
            out = self._ffmpeg_thread.stdout.read(480)
            if out:
                self._mumble.sound_output.add_sound(audioop.mul(out, 2, 0.1))
            else:
                time.sleep(0.01)
