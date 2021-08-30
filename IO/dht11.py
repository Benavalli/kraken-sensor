import time
import Adafruit_DHT
import configparser
import os

from models.temperature_humidity import TemperatureHumidity


class Dht11(object):

    instance = None
    config = configparser.RawConfigParser()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Dht11, cls).__new__(cls)
            cls.config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
            cls.__load_dht11_sensor(cls.instance)
        return cls.instance

    def __load_dht11_sensor(self):
        self.dht_sensor = Adafruit_DHT.DHT11
        self.dht_sensor_pin = self.config.getint('DHT11', 'dht11.gpio.pin')
        self.retries = self.config.getint('DHT11', 'dht11.retries')
        self.sleepTime = self.config.getfloat('DHT11', 'dht11.sleep.time')

    def get_temperature_humidity(self):
        temperature_humidity_list = []
        for x in range(self.retries):
            temperature_humidity = self.__read_dht11_sensor()
            if temperature_humidity is not None:
                temperature_humidity_list.append(temperature_humidity)
            if x < self.retries - 1:
                time.sleep(self.sleepTime)
        return self.__temperature_humidity_average(temperature_humidity_list)

    def __read_dht11_sensor(self):
        try:
            humidity, temperature = Adafruit_DHT.read(self.dht_sensor, self.dht_sensor_pin)
            if humidity is not None and temperature is not None:
                return TemperatureHumidity(temperature, humidity)
            else:
                return None
        except RuntimeError as error:  # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            return None
        except KeyboardInterrupt:
            print('interrupted!')
            return None

    @staticmethod
    def __temperature_humidity_average(temperature_humidity_list):
        temperature_count = 0
        humidity_count = 0
        list_size = len(temperature_humidity_list)
        for temperature_humidity in temperature_humidity_list:
            temperature_count += temperature_humidity.celsius
            humidity_count += temperature_humidity.humidity
        temperature_average = temperature_count / list_size
        humidity_average = humidity_count / list_size
        return TemperatureHumidity(temperature_average, humidity_average)
