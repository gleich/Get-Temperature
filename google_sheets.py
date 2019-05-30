import gspread
from oauth2client.service_account  import ServiceAccountCredentials


def update_sheet(temp, humidity, date, time):
    """
    Will update the data on the google sheet
    :param temp: temperature from the raspberry pi
    :param humidity: humidity from the raspberry pi
    :param date: current date
    :param time: reading time
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("gs_creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("TH_Program").sheet1
    sheet.update_cell(2, 1, temp)
    sheet.update_cell(2, 2, humidity)
    sheet.update_cell(2, 3, date)
    sheet.update_cell(2, 4, time)
    return None



# Testing:
# update_sheet(23, 34, 2, 3)