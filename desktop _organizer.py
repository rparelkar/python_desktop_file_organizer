from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
from datetime import datetime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            if imageFile(src):
                new_destination = folder_destination_images + "/" + filename
                os.rename(src, new_destination)
            elif docFile(src):
                new_destination = folder_destination_doc + "/" + filename
                os.rename(src, new_destination)
            elif src.__contains__('Screen Shot'):
                new_destination = folder_destination_screenshots + "/" + filename
                os.rename(src, new_destination)
            else:
                new_destination = folder_destination_others + "/" + filename
                os.rename(src, new_destination)
            print(new_destination)

folder_to_track = "/Users/Rahul/Desktop/test"
folder_destination_doc = "/Users/Rahul/Desktop/organizedDesktop/doc"
folder_destination_images = "/Users/Rahul/Desktop/organizedDesktop/images"
folder_destination_screenshots = "/Users/Rahul/Desktop/organizedDesktop/screenshots"
folder_destination_others = "/Users/Rahul/Desktop/organizedDesktop/others"

doc_file_types = (".pdf", ".doc", ".docx", ".txt")
image_file_types = (".jpeg", ".png", ".jpg", ".tiff", ".bmp", ".gif")

def docFile(fileName):
    if fileName.casefold().endswith(doc_file_types):
        return True
    else:
        return False

def imageFile(fileName):
    if fileName.casefold().endswith(image_file_types):
        return True
    elif fileName.__contains__('Screen Shot'):
        return False
    else:
        return False

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
        now = datetime.now()
        print("watchdog working...", now.strftime("%d/%m/%Y %H:%M:%S"))
except KeyboardInterrupt:
        observer.stop()
observer.join
