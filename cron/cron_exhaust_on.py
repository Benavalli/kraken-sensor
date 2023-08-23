from IO.relay import Relay
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    relay = Relay()
    if relay.read_exhaust_relay_state() == RelayStateEnum.DISABLED.value:
        relay.change_exhaust_relay_state(RelayStateEnum.ENABLED.name)