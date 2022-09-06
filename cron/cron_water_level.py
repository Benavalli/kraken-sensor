from IO.relay import Relay
from IO.sen0205 import Sen0205
import time

from models.relay_device import RelayStateEnum
from models.water_level import WaterLevelEnum

if __name__ == "__main__":
    water_level_sensor = Sen0205()
    relay = Relay()

    while True:
        try:
            if water_level_sensor.get_water_level_sensor_state() == WaterLevelEnum.LOW.value and \
                    relay.read_valve_relay_state() == RelayStateEnum.DISABLED.value:
                relay.change_valve_relay_state(RelayStateEnum.ENABLED.name)

            if water_level_sensor.get_water_level_sensor_state() == WaterLevelEnum.HIGH.value and \
                    relay.read_valve_relay_state() == RelayStateEnum.ENABLED.value:
                relay.change_valve_relay_state(RelayStateEnum.DISABLED.name)
                break

            time.sleep(0.3)

        except:
            break
