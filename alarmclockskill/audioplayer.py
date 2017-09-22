class AudioPlayer:
    """ A simple audio player."""

    @staticmethod
    def play(filename, on_done):
        """ Play a file.

        :param filename: the path to the audio file to play.
        :param on_done: callback to execute when playing is done.
        """
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        if on_done:
            on_done()

    @staticmethod
    def stop():
        """ Stop the player. """
        pygame.mixer.init()
        pygame.mixer.music.stop()

    @staticmethod
    def pause():
        """ Pause the player. """
        pygame.mixer.init()
        pygame.mixer.music.pause()

    @staticmethod
    def resume():
        """ Resume the player. """
        pygame.mixer.init()
        pygame.mixer.music.unpause()

