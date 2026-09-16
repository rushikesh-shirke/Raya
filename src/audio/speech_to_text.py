from audio.text_to_speech import say
from ai.assistant import Assistant
import speech_recognition as sr


class VoiceListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone(device_index=1)
        self.assistant = Assistant()

    def listen_once(self):
        print("\nRaya: Listening...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )
            except sr.WaitTimeoutError:
                print("Raya: No speech detected.")
                return None

        print("Raya: Recognizing...")

        try:
            text = self.recognizer.recognize_google(audio)

            print(f"\nYou: {text}") 

            response = self.assistant.respond(text)

            if response:
                print(f"Assistant: {response}\n")
                say(response)

            return text

        except sr.UnknownValueError:
            print("Raya: I couldn't understand that.")
            return None

        except sr.RequestError as error:
            print(f"Raya: Speech recognition error: {error}")
            return None


if __name__ == "__main__":
    listener = VoiceListener()

    while True:
        try:
            listener.listen_once()

        except KeyboardInterrupt:
            print("\nRaya: Stopped.")
            break