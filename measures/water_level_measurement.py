from IO.water_level_controller import WaterLevelController
from models.water_level_sensor import WaterLevelStateEnum

water_level_sensors = WaterLevelController()
result = water_level_sensors.get_water_level_measures()
print("Max level: {} , Min level: {}".format(
    WaterLevelStateEnum(result.max_sensor_state).name,
    WaterLevelStateEnum(result.min_sensor_state).name
))
