from IO.relay_controller import RelayController
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    relay = RelayController()
    relay.change_light_relay_state(RelayStateEnum.DISABLED)
    relay.change_light_two_relay_state(RelayStateEnum.DISABLED)
