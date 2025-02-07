import configparser
import os
import gpiod
import threading
import atexit

from models.relay_device import RelayDeviceEnum, RelayDevice, RelayStateEnum


class RelayController:

    _lock = threading.Lock()
    _config = configparser.RawConfigParser()
    _relays = {}

    def __init__(self):
        self._config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
        self.chip = gpiod.Chip(self._config.get('PI', 'chip'))
        self._loading_connected_relays()

    def _loading_connected_relays(self):
        for relay_enum in RelayDeviceEnum:
            relay = self._setup_device(relay_enum, relay_enum.value)
            if relay:
                self._relays[relay_enum] = relay

    def _setup_device(self, device_enum, config_key):
        try:
            if not self._config.has_option("RELAY", config_key):
                return None

            pin = self._config.getint("RELAY", config_key, fallback=None)

            if pin is None:
                print(f"⚠️ {device_enum.name}, ignored.")
                return None

            return RelayDevice(device_enum.name, pin)

        except Exception as e:
            print(f"⚠️ {device_enum.name}, configuration error: {e}")
            return None

    def _change_relay_state(self, device, state):
        if not device:
            print("⚠️ Something went wrong with relay setup..")
            return None

        line = self.chip.get_line(device.pin)
        print(f"Setting device {device.name}, pin {device.pin} as output.")
        self._set_output(line, device.name)
        line.set_value(state.value)
        print(f"{device.name} is {state.name}.")

    def _set_output(self, line, consumer_name):
        with self._lock:
            try:
                line.release()
            except OSError:
                pass
            line.request(consumer=consumer_name, type=gpiod.LINE_REQ_DIR_OUT)

    def change_light_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.LIGHT], state)

    def change_light_two_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.LIGHT_TWO], state)

    def change_exhaust_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.EXHAUST], state)

    def change_humidifier_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.HUMIDIFIER], state)

    def change_pump_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.PUMP], state)

    def change_fan_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.FAN], state)

    def change_inline_fan_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.INLINE_FAN], state)

    def change_valve_relay_state(self, state):
        return self._change_relay_state(self._relays[RelayDeviceEnum.VALVE], state)

    @classmethod
    def cleanup_all(cls):
        with cls._lock:
            print("🛑 Releasing all relays...")
            for relay in cls._relays.values():
                try:
                    relay.line.release()
                    print(f"Relay {relay.name} released.")
                except Exception as e:
                    print(f"⚠️ Error releasing relay {relay.name}: {e}")

            cls._relays.clear()
            print("✅ All relays were released.")

atexit.register(RelayController.cleanup_all)
