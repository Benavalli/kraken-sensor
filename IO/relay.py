import RPi.GPIO as GPIO
import configparser
import os

from models.relay_device import RelayDeviceEnum, RelayDevice, RelayStateEnum
from data import db_manager
from data.db_tables import Events
from datetime import datetime


class Relay(object):

    instance = None
    config = configparser.RawConfigParser()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Relay, cls).__new__(cls)
            GPIO.setwarnings(False)
            # Setting GPIO pin numbers
            if GPIO.getmode() != GPIO.BCM:
                GPIO.setmode(GPIO.BCM)
            cls.config.read(os.path.join(os.path.dirname(__file__), '../config.properties'))
            cls.__loading_connected_relays(cls.instance)
        return cls.instance

    def __loading_connected_relays(self):
        relay_light_pin = self.config.getint('RELAY', 'light.gpio.pin')
        relay_light_state = self.__setup_device(relay_light_pin)
        self.relay_light_device = RelayDevice(
            RelayDeviceEnum.LIGHT.name,
            relay_light_pin,
            RelayStateEnum(relay_light_state).name
        )

        relay_exhaust_pin = self.config.getint('RELAY', 'exhaust.gpio.pin')
        relay_exhaust_state = self.__setup_device(relay_exhaust_pin)
        self.relay_exhaust_device = RelayDevice(
            RelayDeviceEnum.EXHAUST.name,
            relay_exhaust_pin,
            RelayStateEnum(relay_exhaust_state).name
        )

        relay_humidifier_pin = self.config.getint('RELAY', 'humidifier.gpio.pin')
        relay_humidifier_state = self.__setup_device(relay_humidifier_pin)
        self.relay_humidifier_device = RelayDevice(
            RelayDeviceEnum.HUMIDIFIER.name,
            relay_humidifier_pin,
            RelayStateEnum(relay_humidifier_state).name
        )

        relay_pump_pin = self.config.getint('RELAY', 'pump.gpio.pin')
        relay_pump_state = self.__setup_device(relay_pump_pin)
        self.relay_pump_device = RelayDevice(
            RelayDeviceEnum.PUMP.name,
            relay_pump_pin,
            RelayStateEnum(relay_pump_state).name
        )

        relay_fan_pin = self.config.getint('RELAY', 'fan.gpio.pin')
        relay_fan_state = self.__setup_device(relay_fan_pin)
        self.relay_fan_device = RelayDevice(
            RelayDeviceEnum.FAN.name,
            relay_fan_pin,
            RelayStateEnum(relay_fan_state).name
        )

        relay_inline_fan_pin = self.config.getint('RELAY', 'inline.fan.gpio.pin')
        relay_inline_fan_state = self.__setup_device(relay_inline_fan_pin)
        self.relay_inline_fan_device = RelayDevice(
            RelayDeviceEnum.INLINE_FAN.name,
            relay_inline_fan_pin,
            RelayStateEnum(relay_inline_fan_state).name
        )

        relay_valve_pin = self.config.getint('RELAY', 'valve.gpio.pin')
        relay_valve_state = self.__setup_device(relay_valve_pin)
        self.relay_valve_device = RelayDevice(
            RelayDeviceEnum.VALVE.name,
            relay_valve_pin,
            RelayStateEnum(relay_valve_state).name
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

    def read_fan_relay_state(self):
        fan_relay_state = GPIO.input(self.relay_fan_device.pin)
        return fan_relay_state

    def read_inline_fan_relay_state(self):
        inline_fan_relay_state = GPIO.input(self.relay_inline_fan_device.pin)
        return inline_fan_relay_state

    def read_valve_relay_state(self):
        valve_relay_state = GPIO.input(self.relay_valve_device.pin)
        return valve_relay_state

    def change_light_relay_state(self, state):
        GPIO.output(self.relay_light_device.pin, RelayStateEnum[state].value)
        self.relay_light_device.state = RelayStateEnum[state].name
        self.__log_db_event(self.relay_light_device)
        return self.relay_light_device

    def change_exhaust_relay_state(self, state):
        GPIO.output(self.relay_exhaust_device.pin, RelayStateEnum[state].value)
        self.relay_exhaust_device.state = RelayStateEnum[state].name
        self.__log_db_event(self.relay_exhaust_device)
        return self.relay_exhaust_device

    def change_humidifier_relay_state(self, state):
        GPIO.output(self.relay_humidifier_device.pin, RelayStateEnum[state].value)
        self.relay_humidifier_device.state = RelayStateEnum[state].name
        self.__log_db_event(self.relay_humidifier_device)
        return self.relay_humidifier_device

    def change_pump_relay_state(self, state):
        GPIO.output(self.relay_pump_device.pin, RelayStateEnum[state].value)
        self.relay_pump_device.state = RelayStateEnum[state].name
        self.__log_db_event(self.relay_pump_device)
        return self.relay_pump_device

    def change_fan_relay_state(self, state):
        GPIO.output(self.relay_fan_device.pin, RelayStateEnum[state].value)
        self.relay_fan_device.state = RelayStateEnum[state].name
        self.__log_db_event(self.relay_fan_device)
        return self.relay_fan_device

    def change_inline_fan_relay_state(self, state):
        GPIO.output(self.relay_inline_fan_device.pin, RelayStateEnum[state].value)
        self.relay_inline_fan_device.state = RelayStateEnum[state].name
        self.__log_db_event(self.relay_inline_fan_device)
        return self.relay_inline_fan_device

    def change_valve_relay_state(self, state):
        GPIO.output(self.relay_valve_device.pin, RelayStateEnum[state].value)
        self.relay_valve_device.state = RelayStateEnum[state].name
        self.__log_db_event(self.relay_valve_device)
        return self.relay_valve_device

    def get_device_list(self):
        return [
            self.relay_light_device,
            self.relay_exhaust_device,
            self.relay_humidifier_device,
            self.relay_pump_device,
            self.relay_fan_device,
            self.relay_inline_fan_device,
            self.relay_valve_device
        ]
    
    def __log_db_event(self, relay_device):
        engine = db_manager.get_engine()
        event_object = Events(
            date = datetime.now(), 
            device = relay_device.device, 
            state = relay_device.state
        )
        db_manager.persist_object(engine, event_object)
