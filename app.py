from selenium import webdriver
import config

'''
this code requiers Firefox 80.0.1 and geckodriver-v0.27.0-win64
config file should contain login and password variables
'''

browser = webdriver.Firefox()
browser.get("https:github.com")


sign_in = browser.find_element_by_link_text("Sign in")
sign_in.click()


user_name_box = browser.find_element_by_id("login_field")
user_name_box.send_keys(config.login)
password_box = browser.find_element_by_id("password")
password_box.send_keys(config.passw)
password_box.submit()


browser.implicitly_wait(2)
market = browser.find_elements_by_class_name("js-selected-navigation-item")
market[2].click()
browser.save_screenshot("screenshot.png")
browser.quit()

