
import os
from gtts import gTTS
from config import AUDIO_DIR


class VoiceEngine:

    def __init__(self):
        os.makedirs(AUDIO_DIR, exist_ok=True)

    def generate(
        self,
        script,
        filename="voice.mp3",
        language="hi"
    ):

        if not script.strip():
            raise Exception("Script is empty.")

        output = os.path.join(
            AUDIO_DIR,
            filename
        )

        voice = gTTS(
            text=script,
            lang=language,
            slow=False
        )

        voice.save(output)

        return output

    def supported_languages(self):

        return {
            "Hindi": "hi",
            "English": "en",
            "Urdu": "ur"
        }
