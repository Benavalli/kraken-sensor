from IO.dht11 import Dht11

if __name__ == "__main__":
    dht11 = Dht11()
    dht11.get_temperature_humidity().print_temperature_humidity
