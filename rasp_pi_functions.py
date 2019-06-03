import Adafruit_DHT
import RPi.GPIO as GPIO
import datetime_functions as DF


def get_DHT11_output():
    """
    Gets the data from the DHT11 Temperature and Humidity Sensor.
    :return: array where index zero is temp and index and index one is humidity.
    """
    data = []
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    data.append(temperature)
    data.append(humidity)
    return data


# Testing
# print(get_DHT11_output())


def light(pin):
    """
    Will light the blue light. This light is to show that program is running
    :param pin: the GPIO pin number of the LED.
    :param high: if the light should be high or low. Boolean
    :return: None
    """
    if DF.day_time():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.OUT)
        p = GPIO.PWM(7, 100)
        p.start(0)
        p.stop()
