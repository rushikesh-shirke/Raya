"""
detector.py

Smash Enhanced - Impact Detection Engine

This module is responsible ONLY for deciding whether an incoming
audio chunk represents a physical impact.

It does NOT:
    - Read the microphone
    - Play sounds
    - Handle the tray icon

It simply returns:
    True  -> Impact detected
    False -> No impact
"""


class ImpactDetector:
    def __init__(self):
        """
        Initialize detector state.

        We'll add calibration values and history buffers later.
        """
        pass

    def process(self, audio_chunk):
        """
        Analyze one chunk of audio.

        Parameters
        ----------
        audio_chunk :
            One processed chunk of microphone samples.

        Returns
        -------
        bool
            True if an impact is detected.
            False otherwise.
        """
        return False