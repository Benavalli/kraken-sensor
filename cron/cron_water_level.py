from IO.sen0205 import Sen0205
import time

if __name__ == "__main__":
    water_level_sensor = Sen0205()
    while True:
        print(water_level_sensor.get_water_level_sensor_state())
        time.sleep(1.0)
