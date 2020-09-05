from selenium import webdriver
import openpyxl
import seler

workbook = openpyxl.load_workbook("config_file.xlsx")
sheet = workbook["Config"]

for row in range(2, sheet.max_row +1):
    login = sheet.cell(row, 1).value
    passw = sheet.cell(row, 2).value
    repo = sheet.cell(row, 3).value
    if login == None or passw == None or repo == None:
        break
    seler.selerium()

