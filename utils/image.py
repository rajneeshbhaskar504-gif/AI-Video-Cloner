
import os

class ImageEngine:

    def __init__(self):
        pass

    def generate(self, prompt, output_folder="outputs/images"):

        if not prompt.strip():
            raise ValueError("Prompt is empty.")

        os.makedirs(output_folder, exist_ok=True)

        filename = "scene_001.txt"
        output_file = os.path.join(output_folder, filename)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("Image Prompt:\n\n")
            f.write(prompt)

        return {
            "status": True,
            "prompt": prompt,
            "output": output_file
        }

    def multiple(self, prompts, output_folder="outputs/images"):

        results = []

        for prompt in prompts:
            results.append(self.generate(prompt, output_folder))

        return results
