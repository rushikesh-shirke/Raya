from tts import say
from assistant import Assistant
import speech_recognition as sr


class VoiceListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone(device_index=1)
        self.assistant = Assistant()

    def listen_once(self):
        print("\nImpactFX: Listening...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )
            except sr.WaitTimeoutError:
                print("ImpactFX: No speech detected.")
                return None

        print("ImpactFX: Recognizing...")

        try:
            text = self.recognizer.recognize_google(audio)

            print(f"\nYou: {text}") 

            response = self.assistant.respond(text)

            if response:
                print(f"Assistant: {response}\n")
                say(response)

            return text

        except sr.UnknownValueError:
            print("ImpactFX: I couldn't understand that.")
            return None

        except sr.RequestError as error:
            print(f"ImpactFX: Speech recognition error: {error}")
            return None


if __name__ == "__main__":
    listener = VoiceListener()

    while True:
        try:
            listener.listen_once()

        except KeyboardInterrupt:
            print("\nImpactFX: Stopped.")
            break