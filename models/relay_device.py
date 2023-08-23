import enum


class RelayDeviceEnum(enum.Enum):
    LIGHT = 1
    EXHAUST = 2
    HUMIDIFIER = 3
    PUMP = 4
    FAN = 5
    INLINE_FAN = 6
    VALVE = 7
    AIR_PUMP = 8


class RelayStateEnum(enum.Enum):
    ENABLED = 0
    DISABLED = 1


class RelayDevice:

    def __init__(self, device, pin, state):
        self.device = device
        self.pin = pin
        self.state = state
