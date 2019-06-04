import rasp_pi_functions as RPF
import datetime_functions as DF
import google_sheets as GS
import time
import gspread
from oauth2client.service_account  import ServiceAccountCredentials
import json
import RPi.GPIO as GPIO


def main():
    """
    Runs the whole program
    """
    print("Started to get information")
    DHT11_info = RPF.get_DHT11_output()
    current_temperature = DHT11_info[0]
    print("Got temp")
    current_humidity = DHT11_info[1]
    print("Got Humidity")
    current_date = DF.current_date()
    print("Got Current Date")
    current_time = DF.current_time()
    print("Got current time")
    temp_fahrenheit = str(int((float(current_temperature) * (9 / 5)) + 32))
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("gs_creds.json", scope)
    client = gspread.authorize(creds)
    newest_info_sheet = client.open("TH_Newest").sheet1
    stored_sheet = client.open("TH_Stored").sheet1
    GS.update_new_version_sheet(current_temperature, temp_fahrenheit, current_humidity, current_date, current_time, newest_info_sheet)
    print("Data written to new version sheet")
    GS.update_stored_sheet(current_temperature, current_humidity, current_date, current_time, stored_sheet)
    print("Data written to stored version sheet")
    with open("data.json", "a") as data_json:
        data = [current_temperature, temp_fahrenheit, current_humidity, current_date, current_time]
        json.dump(data, data_json)
        print("Data written to JSON")
        print("\n------------------------------------------\n")


while True:
    if DF.day_time():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20, GPIO.LOW)
        GPIO.setup(21, GPIO.OUT)
        print("Next reading in 3 minutes")
        GPIO.output(21, GPIO.HIGH)
        main()
        GPIO.output(21, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        time.sleep(180)
    else:
        GPIO.cleanup()
        print("Next reading in 3 minutes")
        main()
        time.sleep(180)
