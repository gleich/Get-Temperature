import gspread
from oauth2client.service_account  import ServiceAccountCredentials


def update_new_version_sheet(temp, temp_f, humidity, date, time, sheet):
    """
    Will update the data on the google sheet
    :param temp: temperature from the raspberry pi
    :param temp_f: temperature from the raspberry pi in Fahrenheit
    :param humidity: humidity from the raspberry pi
    :param date: current date
    :param time: reading time
    :param sheet: sheet that will be updated
    """
    sheet.update_cell(2, 1, temp)
    sheet.update_cell(2, 2, temp_f)
    sheet.update_cell(2, 3, humidity)
    sheet.update_cell(2, 4, date)
    sheet.update_cell(2, 5, time)


# Testing:
# update_sheet(23, 34, 2, 3)


def update_stored_sheet(temp, humidity, date, time, sheet):
    """
    Will update the data on the google sheet that is storing all the data
    :param temp: temperature from the raspberry pi
    :param temp_f: temperature from the raspberry pi in Fahrenheit
    :param humidity: humidity from the raspberry pi
    :param date: current date
    :param time: reading time
    :param sheet: sheet that will be updated
    """
    row = [temp, humidity, date, time]
    sheet.insert_row(row, 2)
    sheet.update_cell(480, 1, None)
    sheet.update_cell(480, 2, None)
    sheet.update_cell(480, 3, None)
    sheet.update_cell(480, 4, None)