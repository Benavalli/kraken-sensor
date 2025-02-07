import gpiod
import configparser
import os
import threading

from models.water_level_sensor import WaterLevelMeasurementTypeEnum, WaterLevelSensor, WaterLevelStateEnum, \
    WaterLevelMeasurementResult


class WaterLevelController(object):
    _instance = None
    _config = configparser.RawConfigParser()
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WaterLevelController, cls).__new__(cls)
            cls._config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
            cls.__load_water_level_connected_sensors(cls._instance)
        return cls._instance

    def __load_water_level_connected_sensors(self):
        self.chip = gpiod.Chip(self._config.get('PI', 'chip'))
        self.water_level_max_sensor_pin = self._config.getint('SEN0205', 'sen0205.max.gpio.pin')
        self.water_level_max_sensor = WaterLevelSensor(
            WaterLevelMeasurementTypeEnum.MAX.name,
            self.water_level_max_sensor_pin
        )
        
        self.water_level_min_sensor_pin = self._config.getint('SEN0205', 'sen0205.min.gpio.pin')
        self.water_level_min_sensor = WaterLevelSensor(
            WaterLevelMeasurementTypeEnum.MIN.name,
            self.water_level_min_sensor_pin
        )

    def get_water_level_measures(self):
        with self._lock:
            max_level = self._get_sensor_level(
                self.water_level_max_sensor.pin,
                self.water_level_max_sensor.measurement_type
            )
            min_level = self._get_sensor_level(
                self.water_level_min_sensor.pin,
                self.water_level_min_sensor.measurement_type
            )
            return WaterLevelMeasurementResult(max_level, min_level)

    def _get_sensor_level(self, pin, measurement_type):
        try:
            line = self.chip.get_line(pin)
            line.request(consumer=measurement_type.name, type=gpiod.LINE_REQ_DIR_IN)
            value = line.get_value()
            line.release()
            return WaterLevelStateEnum(value)
        except OSError as e:
            print(f"GPIO error: {e} for {measurement_type.name}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e} when fetching {measurement_type.name} data")
            return None
