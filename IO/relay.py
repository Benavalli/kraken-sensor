import configparser
import os
from gpiozero import LED
from models.relay_device import RelayDeviceEnum, RelayDevice, RelayStateEnum


class Relay(object):

    instance = None
    config = configparser.RawConfigParser()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Relay, cls).__new__(cls)
            cls.config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
            cls.__loading_connected_relays(cls.instance)
        return cls.instance

    def __loading_connected_relays(self):
        """Loads all connected relays from the configuration file."""
        self.relay_light_device = self.__setup_device(RelayDeviceEnum.LIGHT, 'light.gpio.pin')
        self.relay_exhaust_device = self.__setup_device(RelayDeviceEnum.EXHAUST, 'exhaust.gpio.pin')
        self.relay_humidifier_device = self.__setup_device(RelayDeviceEnum.HUMIDIFIER, 'humidifier.gpio.pin')
        self.relay_pump_device = self.__setup_device(RelayDeviceEnum.PUMP, 'pump.gpio.pin')
        self.relay_fan_device = self.__setup_device(RelayDeviceEnum.FAN, 'fan.gpio.pin')
        self.relay_inline_fan_device = self.__setup_device(RelayDeviceEnum.INLINE_FAN, 'inline.fan.gpio.pin')
        self.relay_valve_device = self.__setup_device(RelayDeviceEnum.VALVE, 'valve.gpio.pin')

    def __setup_device(self, device_enum, config_key):
        """Configures a relay device and stores the LED instance."""
        pin = self.config.getint('RELAY', config_key)
        relay = LED(pin)  # ✅ Store the LED instance in the device object
        state = RelayStateEnum.ENABLED.name if relay.is_active else RelayStateEnum.DISABLED.name
        return RelayDevice(device_enum.name, pin, state, relay)

    def __change_relay_state(self, device, state):
        """Changes the state of a relay using its stored LED instance."""
        if RelayStateEnum[state] == RelayStateEnum.ENABLED:
            device.relay.on()  # ✅ Uses the stored LED instance
        else:
            device.relay.off()

        device.state = RelayStateEnum[state].name
        return device

    # ✅ Public Methods (Kept Unchanged)
    def read_light_relay_state(self):
        return self.relay_light_device.state

    def read_exhaust_relay_state(self):
        return self.relay_exhaust_device.state

    def read_humidifier_relay_state(self):
        return self.relay_humidifier_device.state

    def read_pump_relay_state(self):
        return self.relay_pump_device.state

    def read_fan_relay_state(self):
        return self.relay_fan_device.state

    def read_inline_fan_relay_state(self):
        return self.relay_inline_fan_device.state

    def read_valve_relay_state(self):
        return self.relay_valve_device.state

    def change_light_relay_state(self, state):
        return self.__change_relay_state(self.relay_light_device, state)

    def change_exhaust_relay_state(self, state):
        return self.__change_relay_state(self.relay_exhaust_device, state)

    def change_humidifier_relay_state(self, state):
        return self.__change_relay_state(self.relay_humidifier_device, state)

    def change_pump_relay_state(self, state):
        return self.__change_relay_state(self.relay_pump_device, state)

    def change_fan_relay_state(self, state):
        return self.__change_relay_state(self.relay_fan_device, state)

    def change_inline_fan_relay_state(self, state):
        return self.__change_relay_state(self.relay_inline_fan_device, state)

    def change_valve_relay_state(self, state):
        return self.__change_relay_state(self.relay_valve_device, state)

    def get_device_list(self):
        """Returns a list of all configured relays."""
        return [
            self.relay_light_device,
            self.relay_exhaust_device,
            self.relay_humidifier_device,
            self.relay_pump_device,
            self.relay_fan_device,
            self.relay_inline_fan_device,
            self.relay_valve_device
        ]
