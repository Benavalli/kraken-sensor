import json


class TemperatureHumidity:

    def __init__(self, celsius, humidity):
        self.celsius = celsius
        self.fahrenheit = celsius * (9 / 5) + 32
        self.humidity = humidity
        
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def print_temperature_humidity(self):
        print("Temp: {:.1f} C / {:.1f} F    Humidity: {}% ".format(self.celsius, self.fahrenheit, self.humidity))
