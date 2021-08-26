import json
import RPi.GPIO as GPIO
import enum


class RelayDeviceEnum(enum.Enum):
    LIGHT = 1
    EXHAUST = 2
    HUMIDIFIER = 3
    PUMP = 4


class RelayStateEnum(enum.Enum):
    ENABLED = 0
    DISABLED = 1


class RelayDevice:

    def __init__(self, device, pin, state):
        self.device = device
        self.pin = pin
        self.state = state

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
