import time
import board
import Adafruit_DHT

from Models.temperature_humidity import TemperatureHumidity


class Dht11:

    DHT_SENSOR = Adafruit_DHT.DHT11
    DHT_PIN = 4
    retries = 5
    sleepTime = 2.0

    def get_temperature_humidity(self):
        temperature_humidity_list = []
        for x in range(self.retries):
            temperature_humidity = self.__read_dht11_sensor()
            if temperature_humidity is not None:
                temperature_humidity_list.append(temperature_humidity)
        return self.__temperature_humidity_average(temperature_humidity_list)

    def __read_dht11_sensor(self):
        try:
            time.sleep(2.0)
            humidity, temperature = Adafruit_DHT.read(self.DHT_SENSOR, self.DHT_PIN)
            if humidity is not None and temperature is not None:
                return TemperatureHumidity(temperature, humidity)
            else:
                return None
        except RuntimeError as error:  # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            return None
        except KeyboardInterrupt:
            print('interrupted!')
            GPIO.cleanup()
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
