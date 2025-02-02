import time
import gpiod
import configparser
import os
import threading

from models.temperature_humidity import TemperatureHumidity


class Dht11(object):

    _instance = None
    _config = configparser.RawConfigParser()
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Dht11, cls).__new__(cls)
            cls._config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
            cls.__load_dht11_sensor(cls._instance)
        return cls._instance

    def __load_dht11_sensor(self):
        self.dht_sensor_pin = self._config.getint('DHT11', 'dht11.gpio.pin')
        self.retries = self._config.getint('DHT11', 'dht11.retries')
        self.sleepTime = self._config.getfloat('DHT11', 'dht11.sleep.time')
        self.chip = gpiod.Chip(self._config.get('PI', 'chip'))

    def get_temperature_humidity(self):
        with self._lock:
            temperature_humidity_list = []
            for x in range(self.retries):
                temperature_humidity = self._read_dht11_sensor()
                if temperature_humidity is not None:
                    temperature_humidity_list.append(temperature_humidity)
                if x < self.retries - 1:
                    time.sleep(self.sleepTime)
            return self.__temperature_humidity_average(temperature_humidity_list)

    def _read_dht11_sensor(self):
        try:
            line = self.chip.get_line(self.dht_sensor_pin)
            try:
                line.release()
            except OSError:
                pass

            line.request(consumer="dht11_control", type=gpiod.LINE_REQ_DIR_OUT)
            line.set_value(0)
            time.sleep(0.018)
            line.set_value(1)
            time.sleep(0.00004)
            line.release()
            line.request(consumer="dht11_status", type=gpiod.LINE_REQ_DIR_IN)

            if not self.__wait_for_signal(line, expected_value=0, timeout=0.1):
                print("Timeout waiting for DHT11 response.")
                line.release()
                return None

            data = []
            for _ in range(40):
                if not self.__wait_for_signal(line, expected_value=1, timeout=0.1):
                    print("Timeout on LOW-HIGH transition.")
                    line.release()
                    return None

                start_time = time.time()
                if not self.__wait_for_signal(line, expected_value=0, timeout=0.1):
                    print("Timeout on HIGH-LOW transition.")
                    line.release()
                    return None

                duration = time.time() - start_time
                data.append(1 if duration > 0.00005 else 0)  # If HIGH > 50µs, it's '1'

            line.release()

            humidity = int("".join(map(str, data[0:8])), 2)
            temperature = int("".join(map(str, data[16:24])), 2)

            return TemperatureHumidity(temperature, humidity)

        except OSError as e:
            print(f"GPIO error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    @staticmethod
    def __wait_for_signal(line, expected_value, timeout):
        start_time = time.time()
        while line.get_value() != expected_value:
            if time.time() - start_time > timeout:
                return False
        return True

    @staticmethod
    def __temperature_humidity_average(temperature_humidity_list):
        temperature_count = 0
        humidity_count = 0
        list_size = len(temperature_humidity_list)
        for temperature_humidity in temperature_humidity_list:
            temperature_count += temperature_humidity.temp
            humidity_count += temperature_humidity.humidity
        temperature_average = temperature_count / list_size
        humidity_average = humidity_count / list_size
        return TemperatureHumidity(temperature_average, humidity_average)
