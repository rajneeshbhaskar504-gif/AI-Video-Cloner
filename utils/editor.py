
from utils.ai import AIEngine
from utils.image import ImageEngine
from utils.voice import VoiceEngine
from utils.video import VideoEngine


class VideoEditor:

    def __init__(self):

        self.ai = AIEngine()
        self.image = ImageEngine()
        self.voice = VoiceEngine()
        self.video = VideoEngine()

    def create_video(
        self,
        topic,
        language="Hindi",
        duration=5
    ):

        # 1. Generate Script
        script = self.ai.generate_script(
            topic,
            language,
            duration
        )

        # 2. Generate Scene Prompts
        prompts = self.ai.generate_scene_prompts(
            script
        )

        # 3. Generate Images
        images = self.image.generate_multiple(
            prompts
        )

        # 4. Generate Voice
        lang = "hi"

        if language == "English":
            lang = "en"

        audio = self.voice.generate(
            script,
            language=lang
        )

        # 5. Create Final Video
        video = self.video.create(
            images,
            audio
        )

        return {
            "script": script,
            "prompts": prompts,
            "images": images,
            "audio": audio,
            "video": video
        }
