from IO.relay import Relay
from IO.water_level_sensors import WaterLevelSensors
import time

from models.relay_device import RelayStateEnum
from models.water_level_sensor import WaterLevelStateEnum

if __name__ == "__main__":
    water_level_sensors = WaterLevelSensors()
    relay = Relay()

    # Check if the water level is low, then activate the relay if needed
    if water_level_sensors.get_water_min_level_sensor_state() == WaterLevelStateEnum.LOW.value:
         if relay.read_valve_relay_state() == RelayStateEnum.DISABLED.value:
                    relay.change_valve_relay_state(RelayStateEnum.ENABLED.name)

         try:
             while water_level_sensors.get_water_max_level_sensor_state() == WaterLevelStateEnum.LOW.value:
                 time.sleep(0.3)
             relay.change_valve_relay_state(RelayStateEnum.DISABLED.name)
         except Exception as e:
             print(f"An error occurred: {e}")
         finally:
             relay.change_valve_relay_state(RelayStateEnum.DISABLED.name)
