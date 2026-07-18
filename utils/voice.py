
import os
from gtts import gTTS

class VoiceEngine:

    def __init__(self, language="hi"):
        self.language = language

    def generate(self, text, output_path):
        if not text.strip():
            raise ValueError("Text is empty.")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        tts = gTTS(
            text=text,
            lang=self.language,
            slow=False
        )

        tts.save(output_path)

        return output_path

    def preview(self, text):
        return text[:100] + "..." if len(text) > 100 else text
