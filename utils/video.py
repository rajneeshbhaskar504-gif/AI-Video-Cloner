
import os
from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips
)
from config import VIDEO_DIR


class VideoEngine:

    def __init__(self):
        os.makedirs(VIDEO_DIR, exist_ok=True)

    def create(
        self,
        image_files,
        audio_file,
        filename="final_video.mp4",
        fps=30
    ):

        if len(image_files) == 0:
            raise Exception("No Images Found.")

        if not os.path.exists(audio_file):
            raise Exception("Audio File Missing.")

        audio = AudioFileClip(audio_file)

        duration = audio.duration / len(image_files)

        clips = []

        for image in image_files:

            clip = (
                ImageClip(image)
                .with_duration(duration)
            )

            clips.append(clip)

        video = concatenate_videoclips(
            clips,
            method="compose"
        )

        video = video.with_audio(audio)

        output = os.path.join(
            VIDEO_DIR,
            filename
        )

        video.write_videofile(
            output,
            fps=fps,
            codec="libx264",
            audio_codec="aac"
        )

        audio.close()
        video.close()

        return output
