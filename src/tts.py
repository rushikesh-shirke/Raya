import asyncio
import edge_tts
import pygame
import time
from pathlib import Path

VOICE = "en-US-AriaNeural"

TEMP_FILE = Path(__file__).parent / "temp.mp3"

pygame.mixer.init()


async def generate_audio(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save(str(TEMP_FILE))


def say(text):
    asyncio.run(generate_audio(text))

    pygame.mixer.music.load(str(TEMP_FILE))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()

    try:
        TEMP_FILE.unlink()
    except Exception:
        pass