import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


src = "C:/Users/vicki/Downloads"
des = "C:/Users/vicki/Documents/Byjus - Python"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Handler Class

class FileMovementHandler(FileSystemEventHandler):

    def on_deleted(self, event):
        file = event.src_path
        file = os.path.basename(file)
        print("Oops! Someone deleted", file)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, src, recursive=True)


# Start the Observer
observer.start()


while True:
    time.sleep(2)
    print("running...")

    