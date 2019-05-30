import rasp_pi_functions as RPF
import datetime_functions as DF
import google_sheets as GS
import time


def main():
    """
    Runs the whole program
    """
    DHT11_info = RPF.get_DHT11_output()
    current_temperature = DHT11_info[0]
    current_humidity = DHT11_info[1]
    current_date = DF.current_date()
    current_time = DF.current_time()
    GS.update_sheet(current_temperature, current_humidity, current_date, current_time)


while True:
    main()
    time.sleep(20)