
import os

class TranscriptEngine:
    def __init__(self):
        self.supported_text = [".txt"]

    def load_text_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        ext = os.path.splitext(file_path)[1].lower()

        if ext not in self.supported_text:
            raise ValueError("Only .txt transcript files are supported.")

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    def get_transcript(self, text):
        if not text:
            return ""

        text = text.replace("\n", " ")
        text = " ".join(text.split())

        return text

    def save_transcript(self, transcript, output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript)

        return output_file
