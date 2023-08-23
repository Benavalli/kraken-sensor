from IO.dht11 import Dht11

if __name__ == "__main__":
    dht11 = Dht11()
    temperature_humidity = dht11.get_temperature_humidity()
    print("Temp: {:.1f} C / {:.1f} F    Humidity: {}% "
          .format(temperature_humidity.temp, temperature_humidity.temp * (9 / 5) + 32, temperature_humidity.humidity))
