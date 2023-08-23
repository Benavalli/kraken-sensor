from IO.relay import Relay
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    relay = Relay()
    if relay.read_valve_relay_state() == RelayStateEnum.ENABLED.value:
        relay.change_valve_relay_state(RelayStateEnum.DISABLED.name)
