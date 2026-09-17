import threading
class AudioRouter:
    """Routes microphone audio to additional consumers without blocking the real time audio callback"""

    def __init__(self):
        self.voice_enabled = False
        self.voice_callback = None

    def set_voice_callback(self, callback):
        self.voice_callback = callback

    def enable_voice(self):
        self.voice_enabled = True

    def disable_voice(self):
        self.voice_enabled = False

    def process(self, audio_data):
        if not self.voice_enabled:
            return

        if self.voice_callback is None:
            return

        audio_copy = audio_data.copy()

        threading.Thread(target=self.voice_callback, args=(audio_copy,), daemon=True).start()
