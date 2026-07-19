import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "AI Social Media Video Creator"
VERSION = "2.0"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
IMAGE_DIR = os.path.join(OUTPUT_DIR, "images")
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio")
VIDEO_DIR = os.path.join(OUTPUT_DIR, "videos")

for folder in [
    UPLOAD_DIR,
    OUTPUT_DIR,
    IMAGE_DIR,
    AUDIO_DIR,
    VIDEO_DIR
]:
    os.makedirs(folder, exist_ok=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
