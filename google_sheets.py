import gspread
from oauth2client.service_account  import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("gs_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("TH_Program").sheet1

data = sheet.get_all_records()

row = sheet.row_values(3)

insertRow = ["Hello", "5", "red", "blue"]

sheet.insert_row(insertRow, 4)