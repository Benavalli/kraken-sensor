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
    if os.path.isfile(file_name):
        os.remove(file_name)
        
def take_picture():
    camera = picamera.PiCamera()
    print('Preparing Camera...')
    sleep(5)
    print('Taking Picture...')
    
    file_name = '{}/taken-pictures/{}.jpg'.format(
        os.path.dirname(__file__),
        datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
    )
    
    camera.capture(file_name)
    camera.close()
    return file_name
    
def save_picture(file_name):
    with open(file_name, 'rb') as file:
        blob_picture = file.read()
    __persist_picture_object(blob_picture) 
    __delete_picture_file(file_name)     
