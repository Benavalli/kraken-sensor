import RPi.GPIO as GPIO
import configparser

from models.relay_device import RelayDeviceEnum, RelayDevice, RelayStateEnum


class Relay(object):
    instance = None
    config = configparser.RawConfigParser()
    property_path = "..\\config.properties"

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Relay, cls).__new__(cls)
            # Setting GPIO pin numbers
            if GPIO.getmode() != GPIO.BCM:
                GPIO.setmode(GPIO.BCM)
            cls.config.read("config.properties")
            cls.__loading_connected_relays(cls.instance)
        return cls.instance

    def __loading_connected_relays(self):
        relay_light_pin = self.config.getint("PIN", "light.gpio.pin")
        relay_light_state = self.__setup_device(relay_light_pin)
        self.relay_light_device = RelayDevice(
            RelayDeviceEnum.LIGHT.name,
            relay_light_pin,
            RelayStateEnum(relay_light_state).name
        )

        relay_exhaust_pin = self.config.getint("PIN", "exhaust.gpio.pin")
        relay_exhaust_state = self.__setup_device(relay_exhaust_pin)
        self.relay_exhaust_device = RelayDevice(
            RelayDeviceEnum.EXHAUST.name,
            relay_exhaust_pin,
            RelayStateEnum(relay_exhaust_state).name
        )

        relay_humidifier_pin = self.config.getint("PIN", "humidifier.gpio.pin")
        relay_humidifier_state = self.__setup_device(relay_humidifier_pin)
        self.relay_humidifier_device = RelayDevice(
            RelayDeviceEnum.HUMIDIFIER.name,
            relay_humidifier_pin,
            RelayStateEnum(relay_humidifier_state).name
        )

        relay_pump_pin = self.config.getint("PIN", "pump.gpio.pin")
        relay_pump_state = self.__setup_device(relay_pump_pin)
        self.relay_pump_device = RelayDevice(
            RelayDeviceEnum.PUMP.name,
            relay_pump_pin,
            RelayStateEnum(relay_pump_state).name
        )

    @staticmethod
    def __setup_device(pin):
        try:
            state = GPIO.input(pin)
            return state
        except:
            try:
                GPIO.setup(pin, GPIO.OUT)
                state = GPIO.input(pin)
                return state
            except:
                return None

    def read_light_relay_state(self):
        light_relay_state = GPIO.input(self.relay_light_device.pin)
        return light_relay_state

    def read_exhaust_relay_state(self):
        exhaust_relay_state = GPIO.input(self.relay_exhaust_device.pin)
        return exhaust_relay_state

    def read_humidifier_relay_state(self):
        humidifier_relay_state = GPIO.input(self.relay_humidifier_device.pin)
        return humidifier_relay_state

    def read_pump_relay_state(self):
        pump_relay_state = GPIO.input(self.relay_pump_device.pin)
        return pump_relay_state

    def change_light_relay_state(self, state):
        GPIO.output(self.relay_light_device.pin, state)
        self.relay_light_device.state = RelayStateEnum(state).name
        return self.relay_light_device

    def change_exhaust_relay_state(self, state):
        GPIO.output(self.relay_exhaust_device.pin, state)
        self.relay_exhaust_device.state = RelayStateEnum(state).name
        return self.relay_exhaust_device

    def change_humidifier_relay_state(self, state):
        GPIO.output(self.relay_humidifier_device.pin, state)
        self.relay_humidifier_device.state = RelayStateEnum(state).name
        return self.relay_humidifier_device

    def change_pump_relay_state(self, state):
        GPIO.output(self.relay_pump_device.pin, state)
        self.relay_pump_device.state = RelayStateEnum(state).name
        return self.relay_pump_device

    def __change_relay_state(self, pin, state):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(self.relay_pump_device.pin, state)

    def __get_device_list(self):
        return [self.relay_light_device,
                self.relay_exhaust_device,
                self.relay_humidifier_device,
                self.relay_pump_device]
