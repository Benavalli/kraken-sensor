class TemperatureHumidity:

    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity

    def print_temperature_humidity(self):
        print("Temp: {:.1f} C / {:.1f} F    Humidity: {}% "
              .format(self.temp, self.temp * (9 / 5) + 32, self.humidity))
