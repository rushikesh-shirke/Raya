"""
detector.py

Impact detection engine for ImpactFX.

This module contains ONLY the detection algorithm.
It does not know anything about microphones, pygame,
or the system tray.
"""

import time
import numpy as np


class ImpactDetector:
    def __init__(
        self,
        peak_threshold=100,
        quiet_threshold=3000,
        cooldown=0.75,
        history_size=5,
    ):
        self.peak_threshold = peak_threshold
        self.quiet_threshold = quiet_threshold
        self.cooldown = cooldown

        self.last_trigger_time = 0

        self.peak_history = [0] * history_size

    def process(self, filtered_audio):
        """
        Returns True if an impact is detected.
        """

        current_peak = np.max(np.abs(filtered_audio))

        self.peak_history.pop(0)
        self.peak_history.append(current_peak)

        now = time.time()

        if now - self.last_trigger_time < self.cooldown:
            return False

        is_clipping = current_peak > self.peak_threshold

        was_quiet = all(
            p < self.quiet_threshold
            for p in self.peak_history[:-2]
        )

        if is_clipping and was_quiet:
            self.last_trigger_time = now
            return True

        return False