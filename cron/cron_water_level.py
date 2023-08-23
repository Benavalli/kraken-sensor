from IO.relay import Relay
from IO.water_level_sensors import WaterLevelSensors
import time

from models.relay_device import RelayStateEnum
from models.water_level_sensor import WaterLevelStateEnum

if __name__ == "__main__":
    water_level_sensors = WaterLevelSensors()
    relay = Relay()

    if water_level_sensors.get_water_min_level_sensor_state() == WaterLevelStateEnum.LOW.value:
         if relay.read_valve_relay_state() == RelayStateEnum.DISABLED.value:
                    relay.change_valve_relay_state(RelayStateEnum.ENABLED.name)
                    
         while True:
            try:
                if water_level_sensors.get_water_max_level_sensor_state == WaterLevelStateEnum.LOW.value:
                    time.sleep(0.3)
                else:
                    relay.change_valve_relay_state(RelayStateEnum.DISABLED.name)
                    break
            except:
                break
