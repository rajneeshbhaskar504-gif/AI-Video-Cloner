
from utils.ai import AIEngine
from utils.voice import VoiceEngine
from utils.image import ImageEngine
from utils.video import VideoEngine


class VideoEditor:

    def __init__(self):

        self.ai = AIEngine()
        self.voice = VoiceEngine()
        self.image = ImageEngine()
        self.video = VideoEngine()

    def create_script(self, topic):

        prompt = f"""
        Write a professional Hindi video script.

        Topic:
        {topic}

        Make it engaging.
        """

        return self.ai.generate(prompt)

    def create_scene_prompts(self, script):

        prompt = f"""
        Divide this script into scenes.

        For every scene create one cinematic AI image prompt.

        Script:

        {script}
        """

        data = self.ai.generate(prompt)

        return data.split("\n")

    def create_voice(self, script):

        return self.voice.generate(
            script,
            "outputs/audio.mp3"
        )

    def create_images(self, prompts):

        images = []

        for prompt in prompts:

            result = self.image.generate(prompt)

            images.append(result["output"])

        return images

    def create_video(self, topic):

        script = self.create_script(topic)

        prompts = self.create_scene_prompts(script)

        audio = self.create_voice(script)

        images = self.create_images(prompts)

        final_video = self.video.create_video(
            images,
            audio
        )

        return {
            "script": script,
            "audio": audio,
            "images": images,
            "video": final_video
        }
