from IO.dht11 import Dht11
from IO.relay import Relay
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    dht11 = Dht11()
    relay = Relay()
    temperature_humidity = dht11.get_temperature_humidity()

    if temperature_humidity.humidity < 45:
        if relay.read_humidifier_relay_state() == RelayStateEnum.DISABLED.value:
            relay.change_humidifier_relay_state(RelayStateEnum.ENABLED.value)
        if relay.read_exhaust_relay_state() == RelayStateEnum.ENABLED.value and temperature_humidity.celsius < 27:
            relay.change_exhaust_relay_state(RelayStateEnum.DISABLED.value)

    if temperature_humidity.humidity > 65:
        if relay.read_humidifier_relay_state() == RelayStateEnum.ENABLED.value:
            relay.change_humidifier_relay_state(RelayStateEnum.DISABLED.value)
        if relay.read_exhaust_relay_state() == RelayStateEnum.DISABLED.value:
            relay.change_exhaust_relay_state(RelayStateEnum.ENABLED.value)

    if temperature_humidity.celsius < 27:
        if relay.read_exhaust_relay_state() == RelayStateEnum.ENABLED.value and temperature_humidity.humidity < 65:
            relay.change_exhaust_relay_state(RelayStateEnum.DISABLED.value)

    if temperature_humidity.celsius > 29:
        if relay.read_exhaust_relay_state() == RelayStateEnum.DISABLED.value:
            relay.change_exhaust_relay_state(RelayStateEnum.ENABLED.value)
