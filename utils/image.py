
import os
import requests
from config import IMAGE_DIR, HUGGINGFACE_API_TOKEN

class ImageEngine:

    def __init__(self):

        if not HUGGINGFACE_API_TOKEN:
            raise Exception("HUGGINGFACE_API_TOKEN not found.")

        self.api_url = (
            "https://router.huggingface.co/hf-inference/models/"
            "black-forest-labs/FLUX.1-schnell"
        )

        self.headers = {
            "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}",
            "Content-Type": "application/json"
        }

    def generate(self, prompt, filename):

        payload = {
            "inputs": prompt
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=300
        )

        if response.status_code != 200:
            raise Exception(response.text)

        os.makedirs(IMAGE_DIR, exist_ok=True)

        output = os.path.join(
            IMAGE_DIR,
            filename
        )

        with open(output, "wb") as f:
            f.write(response.content)

        return output

    def generate_multiple(self, prompts):

        images = []

        for index, prompt in enumerate(prompts):

            filename = f"scene_{index+1}.png"

            image = self.generate(
                prompt,
                filename
            )

            images.append(image)

        return images
