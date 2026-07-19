import os
import requests

class ImageEngine:

    def __init__(self):
        self.api_token = os.getenv("HUGGINGFACE_API_TOKEN")

        self.api_url = (
            "https://router.huggingface.co/hf-inference/models/"
            "black-forest-labs/FLUX.1-schnell"
        )

        self.headers = {
            "Authorization": f"Bearer {self.api_token}"
        }

    def generate(
        self,
        prompt,
        output_folder="outputs/images",
        filename="image.png"
    ):

        os.makedirs(output_folder, exist_ok=True)

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={
                "inputs": prompt
            },
            timeout=300
        )

        if response.status_code != 200:
            raise Exception(response.text)

        output_path = os.path.join(
            output_folder,
            filename
        )

        with open(output_path, "wb") as f:
            f.write(response.content)

        return output_path
