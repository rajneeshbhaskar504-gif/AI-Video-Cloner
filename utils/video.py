
import os
from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips
)


class VideoEngine:

    def __init__(self, fps=24):
        self.fps = fps

    def create_video(
        self,
        image_files,
        audio_file,
        output_file="outputs/final_video.mp4"
    ):

        if not image_files:
            raise ValueError("No images found.")

        if not os.path.exists(audio_file):
            raise FileNotFoundError(audio_file)

        audio = AudioFileClip(audio_file)

        duration = audio.duration / len(image_files)

        clips = []

        for image in image_files:

            if not os.path.exists(image):
                continue

            clip = (
                ImageClip(image)
                .with_duration(duration)
            )

            clips.append(clip)

        if not clips:
            raise ValueError("No valid image clips.")

        final_video = concatenate_videoclips(
            clips,
            method="compose"
        )

        final_video = final_video.with_audio(audio)

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        final_video.write_videofile(
            output_file,
            fps=self.fps,
            codec="libx264",
            audio_codec="aac"
        )

        audio.close()
        final_video.close()

        return output_file
