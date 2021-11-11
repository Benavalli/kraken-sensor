import RPi.GPIO as GPIO
import configparser
import os


class Sen0205(object):

    instance = None
    config = configparser.RawConfigParser()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Sen0205, cls).__new__(cls)
            # Setting GPIO pin numbers
            if GPIO.getmode() != GPIO.BCM:
                GPIO.setmode(GPIO.BCM)
            cls.config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
            cls.__load_water_level_sensor(cls.instance)
        return cls.instance

    def __load_water_level_sensor(self):
        self.water_level_sensor_pin = self.config.getint('SEN0205', 'sen0205.gpio.pin')
        GPIO.setup(self.water_level_sensor_pin, GPIO.IN)

    def get_water_level_sensor_state(self):
        return GPIO.input(self.water_level_sensor_pin)
