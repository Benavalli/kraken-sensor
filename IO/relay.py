import configparser
import os
import gpiod

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
        """Carrega todos os relés do arquivo de configuração e mantém o estado."""
        self.relays = {
            RelayDeviceEnum.LIGHT: self.__setup_device(RelayDeviceEnum.LIGHT, 'light.gpio.pin'),
            RelayDeviceEnum.EXHAUST: self.__setup_device(RelayDeviceEnum.EXHAUST, 'exhaust.gpio.pin'),
            RelayDeviceEnum.HUMIDIFIER: self.__setup_device(RelayDeviceEnum.HUMIDIFIER, 'humidifier.gpio.pin'),
            RelayDeviceEnum.PUMP: self.__setup_device(RelayDeviceEnum.PUMP, 'pump.gpio.pin'),
            RelayDeviceEnum.FAN: self.__setup_device(RelayDeviceEnum.FAN, 'fan.gpio.pin'),
            RelayDeviceEnum.INLINE_FAN: self.__setup_device(RelayDeviceEnum.INLINE_FAN, 'inline.fan.gpio.pin'),
            RelayDeviceEnum.VALVE: self.__setup_device(RelayDeviceEnum.VALVE, 'valve.gpio.pin'),
        }

    def __setup_device(self, device_enum, config_key):
        """Configura um dispositivo de relé e mantém seu estado."""
        pin = self.config.getint('RELAY', config_key)
        relay = LED(pin)  # ✅ Armazena a instância de LED para manter estado
        state = RelayStateEnum.ENABLED.name if relay.is_active else RelayStateEnum.DISABLED.name
        return RelayDevice(device_enum.name, pin, state, relay)

    def __change_relay_state(self, device, state):
        """Altera o estado do relé e mantém o estado ligado."""
        if RelayStateEnum[state] == RelayStateEnum.ENABLED:
            device.relay.on()
        else:
            device.relay.off()

        device.state = RelayStateEnum[state].name
        return device

    # ✅ Métodos públicos mantidos
    def read_light_relay_state(self):
        return self.relays[RelayDeviceEnum.LIGHT].state

    def read_exhaust_relay_state(self):
        return self.relays[RelayDeviceEnum.EXHAUST].state

    def read_humidifier_relay_state(self):
        return self.relays[RelayDeviceEnum.HUMIDIFIER].state

    def read_pump_relay_state(self):
        return self.relays[RelayDeviceEnum.PUMP].state

    def read_fan_relay_state(self):
        return self.relays[RelayDeviceEnum.FAN].state

    def read_inline_fan_relay_state(self):
        return self.relays[RelayDeviceEnum.INLINE_FAN].state

    def read_valve_relay_state(self):
        return self.relays[RelayDeviceEnum.VALVE].state

    def change_light_relay_state(self, state):
        return self.__change_relay_state(self.relays[RelayDeviceEnum.LIGHT], state)

    def change_exhaust_relay_state(self, state):
        return self.__change_relay_state(self.relays[RelayDeviceEnum.EXHAUST], state)

    def change_humidifier_relay_state(self, state):
        return self.__change_relay_state(self.relays[RelayDeviceEnum.HUMIDIFIER], state)

    def change_pump_relay_state(self, state):
        return self.__change_relay_state(self.relays[RelayDeviceEnum.PUMP], state)

    def change_fan_relay_state(self, state):
        return self.__change_relay_state(self.relays[RelayDeviceEnum.FAN], state)

    def change_inline_fan_relay_state(self, state):
        return self.__change_relay_state(self.relays[RelayDeviceEnum.INLINE_FAN], state)

    def change_valve_relay_state(self, state):
        return self.__change_relay_state(self.relays[RelayDeviceEnum.VALVE], state)

    def get_device_list(self):
        """Retorna uma lista de todos os relés configurados."""
        return list(self.relays.values())
