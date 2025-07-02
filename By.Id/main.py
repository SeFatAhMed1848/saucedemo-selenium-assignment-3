from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    #open website
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    return driver

def login_with_attribute(driver, username, password):

    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys(username)
    time.sleep(2)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)
    time.sleep(2)

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)  # Wait for login to complete

# Run
driver = open_browser()
login_with_attribute(driver, "standard_user", "secret_sauce")
time.sleep(4) # to see view result , previous time for just opening link time

driver.quit()