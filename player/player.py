from __future__ import unicode_literals

import vlc


class Player(object):
    _volume_state_for_mute = 0

    def __init__(self, stream):
        self._player = vlc.MediaPlayer(stream)

    def play(self):
        return self._player.play()

    def pause(self):
        return self._player.pause()

    def stop(self):
        return self._player.stop()

    def get_volume(self):
        return self._player.audio_get_volume()

    def set_volume(self, value):
        return self._player.audio_set_volume(value)

    def mute(self):
        self._volume_state_for_mute = self.get_volume()
        return self.set_volume(0)

    def unmute(self):
        self.set_volume(self._volume_state_for_mute)
        self._volume_state_for_mute = 0
        return 0

    @property
    def state(self):
        return self._player.get_state()

    @property
    def is_playing(self):
        return self.state == vlc.State.Playing

    @property
    def is_paused(self):
        return self.state == vlc.State.Paused

    @property
    def is_stopped(self):
        return self.state == vlc.State.Stopped

    @property
    def is_broken(self):
        return self.state == vlc.State.Error
