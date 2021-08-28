from IO.relay import Relay
from models.relay_device import RelayStateEnum
import sys
sys.path.append("/home/pi/Kraken/kraken-sensor")

if __name__ == "__main__":
    if Relay().read_light_relay_state() == RelayStateEnum.ENABLED.value:
        print("ativo")
    else:
        print("inativo")
        Relay().change_light_relay_state(RelayStateEnum.ENABLED.value)

