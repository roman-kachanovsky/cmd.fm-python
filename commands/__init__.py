from __future__ import absolute_import

from . import genres, play, pause, resume, next, previous, info, volume, quit


commands = [
    genres.Genres,
    play.Play,
    play.P,
    pause.Pause,
    resume.Resume,
    next.Next,
    next.Skip,
    previous.Previous,
    previous.Prev,
    previous.Back,
    info.Info,
    info.I,
    info.Information,
    volume.Volume,
    volume.V,
    volume.Vol,
    quit.Quit,
    quit.Q,
]
