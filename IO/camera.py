from time import sleep
from datetime import datetime
from data import db_manager
from data.db_tables import Pictures

import picamera
import os

def take_picture():
    camera = picamera.PiCamera()
    print('Preparing Camera...')
    sleep(5)
    print('Taking Picture...')
    file_name = datetime.now() + ".jpg"
    return camera.capture(datetime.now() + ".jpg")

def save_picture_blob(picture):
    with open(picture, 'rb') as file:
        blobData = file.read()
    engine = db_manager.get_engine()
    blob_data = file.read()
    picture_object = Pictures(date = datetime.now(), picture = blobData)
    db_manager.persist_object(engine, picture_object)

def delete_saved_picture(picture):
    if os.path.isfile(picture):
        os.remove(picture)
        