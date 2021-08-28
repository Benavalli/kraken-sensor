import os
user_home = os.environ["KRAKEN_SENSOR_HOME"]
from IO.relay import Relay
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    Relay().change_light_relay_state(RelayStateEnum.ENABLED.value)
