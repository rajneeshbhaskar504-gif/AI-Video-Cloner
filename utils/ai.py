
import google.generativeai as genai
from config import GEMINI_API_KEY

class AIEngine:

    def __init__(self):

        if not GEMINI_API_KEY:
            raise Exception(
                "Gemini API Key not found."
            )

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_script(
        self,
        topic,
        language="Hindi",
        duration=5
    ):

        prompt = f"""

Create an original YouTube video script.

Topic:
{topic}

Language:
{language}

Duration:
{duration} Minutes

Rules:

• Original Script
• Engaging
• Professional
• Narration Only
• No Copyright Content

"""

        response = self.model.generate_content(
            prompt
        )

        return response.text

    def generate_scene_prompts(
        self,
        script
    ):

        prompt = f"""

Read this script.

Create one cinematic AI image prompt for every scene.

Only return prompts.

Script:

{script}

"""

        response = self.model.generate_content(
            prompt
        )

        prompts = []

        for line in response.text.split("\n"):

            line = line.strip()

            if line:

                prompts.append(line)

        return prompts
