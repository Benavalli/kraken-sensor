from time import sleep
from datetime import datetime
from data import db_manager
from data.db_tables import Pictures

import picamera
import os
    
def __persist_picture_object(blob_picture):
    engine = db_manager.get_engine()
    picture_object = Pictures(
        date = datetime.now(), 
        picture = blob_picture
    )
    db_manager.persist_object(engine, picture_object)
    
def __delete_picture_file(file_name):
    try:
        os.remove(file_name)
        print(f"Deleted file: {file_name}")
    except FileNotFoundError:
        print(f"Warning: File {file_name} not found.")
    except Exception as e:
        print(f"Error deleting file {file_name}: {e}")
        
def take_picture():
    print('Preparing Camera...')
    sleep(5)
    print('Taking Picture...')

    pictures_dir = os.path.join(os.path.dirname(__file__), 'taken-pictures')
    os.makedirs(pictures_dir, exist_ok=True)

    file_name = os.path.join(
        pictures_dir,
        f"{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.jpg"
    )

    with picamera.PiCamera() as camera:
        camera.capture(file_name)
        return file_name
    
def save_picture(file_name):
    try:
        with open(file_name, 'rb') as file:
            blob_picture = file.read()
        __persist_picture_object(blob_picture)
        __delete_picture_file(file_name)
        print(f"Picture saved and file {file_name} deleted.")
    except Exception as e:
        print(f"Error saving picture: {e}")
