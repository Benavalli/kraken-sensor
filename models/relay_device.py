import enum


class RelayDeviceEnum(enum.Enum):
    LIGHT = "light.gpio.pin"
    LIGHT_TWO = "light.two.gpio.pin"
    EXHAUST = "exhaust.gpio.pin"
    HUMIDIFIER = "humidifier.gpio.pin"
    PUMP = "pump.gpio.pin"
    FAN = "fan.gpio.pin"
    INLINE_FAN = "inline.fan.gpio.pin"
    VALVE = "valve.gpio.pin"
    AIR_PUMP = "air.pump.gpio.pin"


class RelayStateEnum(enum.Enum):
    ENABLED = 0
    DISABLED = 1


class RelayDevice:

    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
