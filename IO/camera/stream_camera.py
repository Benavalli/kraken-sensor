from time import sleep
from IO.camera import base_camera

import picamera
import io


class StreamCamera(base_camera.BaseCamera):
    
    @staticmethod
    def frames():
        with picamera.PiCamera(resolution = '640x480') as camera:
            # let camera warm up
            sleep(5)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
        
