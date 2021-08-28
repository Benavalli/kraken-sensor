from IO.relay import Relay
from models.relay_device import RelayStateEnum
import time

import sys
sys.path.append("/home/pi/Kraken/kraken-sensor")

if __name__ == "__main__":
    relay = Relay()
    time.sleep(2)
    aqui = relay.read_light_relay_state()
    print(aqui + " 1333")

    if relay.read_light_relay_state() == RelayStateEnum.ENABLED.value:
        print("ativo")
    else:
        print("inativo")
        relay.change_light_relay_state(RelayStateEnum.ENABLED.value)

