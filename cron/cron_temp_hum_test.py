from IO.dht11 import Dht11
from IO.relay import Relay
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    dht11 = Dht11()
    relay = Relay()
    temperature_humidity = dht11.get_temperature_humidity()

    print("Termperature:", temperature_humidity.temp)
    print("Humidity:", temperature_humidity.humidity)
