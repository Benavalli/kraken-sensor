from IO.relay import Relay
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    relay = Relay()
    if relay.read_inline_fan_relay_state() == RelayStateEnum.ENABLED.value:
        relay.change_inline_fan_relay_state(RelayStateEnum.DISABLED.name)
