from selenium import webdriver
import openpyxl

#dodaj execeptiony na brak pliku i na błedny plik
workbook = openpyxl.load_workbook("config_file.xlsx")
sheet = workbook["Config"]

for row in range(2, sheet.max_row +1):
    login = sheet.cell(row, 1).value
    passw = sheet.cell(row, 2).value
    if login == None or passw == None:
        break
    browser = webdriver.Firefox()
    browser.get("https:github.com")
    sign_in = browser.find_element_by_link_text("Sign in")
    sign_in.click()
    user_name_box = browser.find_element_by_id("login_field")
    user_name_box.send_keys(login)
    password_box = browser.find_element_by_id("password")
    password_box.send_keys(passw)
    password_box.submit()
    browser.implicitly_wait(2)
    market = browser.find_elements_by_class_name("js-selected-navigation-item")
    market[2].click()
    browser.save_screenshot("screenshot" +str(row)+".png")
    browser.quit()

