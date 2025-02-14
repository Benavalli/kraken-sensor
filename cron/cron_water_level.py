from IO.relay_controller import RelayController
from IO.water_level_controller import WaterLevelController
import time

from models.relay_device import RelayStateEnum
from models.water_level_sensor import WaterLevelStateEnum

if __name__ == "__main__":
    levelController = WaterLevelController()
    relayController = RelayController()

    if levelController.get_water_level_measures().min_sensor_state == WaterLevelStateEnum.LOW:
        print(f"⚠️ Min level low, turning valve on.")
        relayController.change_valve_relay_state(RelayStateEnum.ENABLED)
        time.sleep(1)

        while True:
            try:
                if levelController.get_water_level_measures().max_sensor_state == WaterLevelStateEnum.HIGH:
                    relayController.change_valve_relay_state(RelayStateEnum.DISABLED)
                    print(f"⚠️ Max level HIGH, turning valve off.")
                    break
                else:
                    time.sleep(0.5)
            except Exception as e:
                print(f"Error: {e}.")
                break
