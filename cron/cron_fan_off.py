from IO.relay_controller import RelayController
from models.relay_device import RelayStateEnum

if __name__ == "__main__":
    relayController = RelayController()
    relayController.change_fan_relay_state(RelayStateEnum.DISABLED)
