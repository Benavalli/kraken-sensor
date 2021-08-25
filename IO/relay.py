import RPi.GPIO as GPIO


class Relay:

    # def __init__(self):
    #     # The script as below using BCM GPIO 00..nn numbers
    #     GPIO.setmode(GPIO.BCM)


    def change_light_relay_state(self, activated):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(26, GPIO.OUT)
        if activated is 0:
            GPIO.output(26, GPIO.HIGH)
        else:
            GPIO.output(26, GPIO.LOW)


    def change_exhaust_relay_state(self, activated):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(19, GPIO.OUT)
        if activated is 0:
            GPIO.output(19, GPIO.HIGH)
        else:
            GPIO.output(19, GPIO.LOW)


    def change_humidifier_relay_state(self, activated):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.OUT)
        if activated is 0:
            GPIO.output(13, GPIO.HIGH)
        else:
            GPIO.output(13, GPIO.LOW)


    def change_pump_relay_state(self, activated):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.OUT)
        if activated is 0:
            GPIO.output(5, GPIO.HIGH)
        else:
            GPIO.output(5, GPIO.LOW)
