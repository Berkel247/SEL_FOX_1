import app
from selenium import webdriver


def selerium():
    browser = webdriver.Firefox()
    browser.get("https:github.com")
    sign_in = browser.find_element_by_link_text("Sign in")
    sign_in.click()
    user_name_box = browser.find_element_by_id("login_field")
    user_name_box.send_keys(app.login)
    password_box = browser.find_element_by_id("password")
    password_box.send_keys(app.passw)
    password_box.submit()
    browser.implicitly_wait(2)
    repoz = browser.find_element_by_css_selector("div#repos-container > ul.list-style-none > li > div > a > span[title=" +repo +"]")
    repoz.click()
    browser.save_screenshot("screenshot" +str(app.row)+".png")
    browser.quit()