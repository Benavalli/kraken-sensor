import sys
sys.path.append("/home/pi/Kraken/kraken-sensor/cron")
from IO.relay import Relay
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    Relay().change_light_relay_state(RelayStateEnum.ENABLED.value)
