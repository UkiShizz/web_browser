import os
import requests
from PyQt5.QtCore import QObject, pyqtSignal

import os
import requests
from PyQt5.QtCore import QObject, pyqtSignal

class Downloader(QObject):
    download_started = pyqtSignal(str)
    download_progress = pyqtSignal(int)
    download_finished = pyqtSignal(str)
    download_failed = pyqtSignal(str)

    def __init__(self, download_directory="downloads"):
        super().__init__()
        self.download_directory = download_directory
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

    def download_file(self, url):
        try:
            self.download_started.emit(url)
            response = requests.get(url, stream=True)
            response.raise_for_status()

            file_name = os.path.join(self.download_directory, url.split('/')[-1])
            total_size = int(response.headers.get('content-length', 0))
            chunk_size = 1024
            num_bars = total_size // chunk_size

            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        file.write(chunk)
                        progress = int(file.tell() * 100 / total_size)
                        self.download_progress.emit(progress)

            self.download_finished.emit(file_name)
        except Exception as e:
            self.download_failed.emit(str(e))