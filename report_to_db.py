
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]
credentials = ServiceAccountCredentials.from_json_keyfile_name("wedding_report.json", scopes) #access the json key you downloaded earlier
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
sheet = file.open("Invitatii")  #open sheet

sheet2 = sheet.worksheet("nu particip")
sheet1 = sheet.worksheet("Particip")


def add_confirmation(confirmation, response):
    if response == "True":
        sheet1.append_row(confirmation)
    else:
        sheet2.append_row(confirmation)
