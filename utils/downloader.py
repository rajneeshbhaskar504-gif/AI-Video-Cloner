
import os
import shutil
from datetime import datetime


class DownloadManager:

    def __init__(self):
        self.output_dir = "outputs"
        os.makedirs(self.output_dir, exist_ok=True)

    def save_file(self, source_path):

        if not os.path.exists(source_path):
            raise FileNotFoundError(source_path)

        filename = os.path.basename(source_path)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        new_name = f"{timestamp}_{filename}"

        destination = os.path.join(
            self.output_dir,
            new_name
        )

        shutil.copy2(
            source_path,
            destination
        )

        return destination

    def list_files(self):

        files = []

        for file in os.listdir(self.output_dir):

            path = os.path.join(
                self.output_dir,
                file
            )

            if os.path.isfile(path):
                files.append(path)

        return sorted(files)

    def delete_file(self, file_path):

        if os.path.exists(file_path):
            os.remove(file_path)
            return True

        return False

    def clear_outputs(self):

        for file in self.list_files():
            os.remove(file)

        return True
