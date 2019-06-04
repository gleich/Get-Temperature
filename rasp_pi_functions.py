import Adafruit_DHT


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
