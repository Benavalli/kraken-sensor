import RPi.GPIO as GPIO
import time

if __name__ == "__main__":
    time.sleep(1)
    GPIO.setup(26, GPIO.OUT)
    GPIO.output(26, 0)
    time.sleep(3)