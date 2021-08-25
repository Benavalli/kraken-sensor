import RPi.GPIO as GPIO
import ConfigParser

from Models.relay_device import RelayDeviceEnum, RelayDevice, RelayStateEnum


class Relay(object):
    instance = None
    config = ConfigParser.RawConfigParser()
    property_path = "../config.properties"

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Relay, cls).__new__(cls)
            # Setting GPIO pin numbers
            GPIO.setmode(GPIO.BCM)
            cls.config.read(cls.property_path)
            cls.__loading_connected_relays(cls.instance)
        return cls.instance

    def __del__(self):
        GPIO.cleanup()

    def __loading_connected_relays(self):
        relay_light_pin = self.config.get("PIN", "light.gpio.pin")
        relay_light_state = self.__read_device_state(relay_light_pin)
        self.relay_light_device = RelayDevice(RelayDeviceEnum(1), relay_light_pin, RelayStateEnum(relay_light_state))

        relay_exhaust_pin = self.config.get("PIN", "exhaust.gpio.pin")
        relay_exhaust_state = self.__read_device_state(relay_exhaust_pin)
        self.relay_exhaust_device = RelayDevice(RelayDeviceEnum(2), relay_exhaust_pin,
                                                RelayStateEnum(relay_exhaust_state))

        relay_humidifier_pin = self.config.get("PIN", "humidifier.gpio.pin")
        relay_humidifier_state = self.__read_device_state(relay_humidifier_pin)
        self.relay_humidifier_device = RelayDevice(RelayDeviceEnum(3), relay_humidifier_pin,
                                                   RelayStateEnum(relay_humidifier_state))

        relay_pump_pin = self.config.get("PIN", "pump.gpio.pin")
        relay_pump_state = self.__read_device_state(relay_pump_pin)
        self.relay_pump_device = RelayDevice(RelayDeviceEnum(4), relay_pump_pin, RelayStateEnum(relay_pump_state))

    @staticmethod
    def __read_device_state(pin):
        GPIO.setup(pin, GPIO.IN)
        return GPIO.input(pin)

    def change_light_relay_state(self, state):
        GPIO.setup(self.relay_light_device.pin, GPIO.OUT)
        GPIO.output(self.relay_light_device.pin, RelayStateEnum(state))
        self.relay_light_device.state = RelayStateEnum(state)
        return self.__get_device_list()

    def change_exhaust_relay_state(self, state):
        GPIO.setup(self.relay_exhaust_device.pin, GPIO.OUT)
        GPIO.output(self.relay_exhaust_device.pin, RelayStateEnum(state))
        self.relay_exhaust_device.state = RelayStateEnum(state)
        return self.__get_device_list()

    def change_humidifier_relay_state(self, state):
        GPIO.setup(self.relay_humidifier_device.pin, GPIO.OUT)
        GPIO.output(self.relay_humidifier_device.pin, RelayStateEnum(state))
        self.relay_humidifier_device.state = RelayStateEnum(state)
        return self.__get_device_list()

    def change_pump_relay_state(self, state):
        GPIO.setup(self.relay_pump_device.pin, GPIO.OUT)
        GPIO.output(self.relay_pump_device.pin, RelayStateEnum(state))
        self.relay_pump_device.state = RelayStateEnum(state)
        return self.__get_device_list()

    def __get_device_list(self):
        return {self.relay_light_device, self.relay_exhaust_device, self.relay_humidifier_device,
                self.relay_pump_device}
