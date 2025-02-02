from IO.dht11 import Dht11
from IO.relay_controller import RelayController
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    dht11 = Dht11()
    relayController = RelayController()
    temperature_humidity = dht11.get_temperature_humidity()

    if temperature_humidity.humidity < 84:
        relayController.change_humidifier_relay_state(RelayStateEnum.ENABLED)
        relayController.change_fan_relay_state(RelayStateEnum.ENABLED)

    if temperature_humidity.humidity > 90 :
        relayController.change_humidifier_relay_state(RelayStateEnum.DISABLED)
        relayController.change_fan_relay_state(RelayStateEnum.DISABLED)
