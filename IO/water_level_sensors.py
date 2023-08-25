import RPi.GPIO as GPIO
import configparser
import os

from models.water_level_sensor import WaterLevelMeasurementTypeEnum, WaterLevelSensor, WaterLevelStateEnum


class WaterLevelSensors(object):

    instance = None
    config = configparser.RawConfigParser()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(WaterLevelSensors, cls).__new__(cls)
            # Setting GPIO pin numbers
            if GPIO.getmode() != GPIO.BCM:
                GPIO.setmode(GPIO.BCM)
            cls.config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
            cls.__load_water_level_connected_sensors(cls.instance)
        return cls.instance

    def __load_water_level_connected_sensors(self):
        self.water_level_max_sensor_pin = self.config.getint('SEN0205', 'sen0205.max.gpio.pin')
        GPIO.setup(self.water_level_max_sensor_pin, GPIO.IN)
        self.water_level_max_sensor = WaterLevelSensor(
            WaterLevelMeasurementTypeEnum.MAX.name,
            self.water_level_max_sensor_pin
        )
        
        self.water_level_min_sensor_pin = self.config.getint('SEN0205', 'sen0205.min.gpio.pin')
        GPIO.setup(self.water_level_min_sensor_pin, GPIO.IN)
        self.water_level_min_sensor = WaterLevelSensor(
            WaterLevelMeasurementTypeEnum.MIN.name,
            self.water_level_min_sensor_pin
        )
        
    def get_water_max_level_sensor_state(self):
        return GPIO.input(self.water_level_max_sensor.pin)
        
    def get_water_min_level_sensor_state(self):
        return GPIO.input(self.water_level_min_sensor.pin)
    
    def print_water_level_sensors_state(self):
        max_sensor_level = GPIO.input(self.water_level_max_sensor.pin)
        min_sensor_level = GPIO.input(self.water_level_min_sensor.pin)
        print("Max level: {} , Min level: {}"
            .format(
                WaterLevelStateEnum(max_sensor_level).name,
                WaterLevelStateEnum(min_sensor_level).name 
            )
        )
          
