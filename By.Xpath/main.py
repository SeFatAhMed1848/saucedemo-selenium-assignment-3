from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    return driver

def login_with_xpath(driver, username, password):

    username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
    username_field.send_keys(username)
    time.sleep(2)

    password_field = driver.find_element(By.XPATH, "//input[@id='password']")
    password_field.send_keys(password )
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(2)  # Wait for login to complete

# Run
driver = open_browser()
login_with_xpath(driver, "standard_user", "secret_sauce")
time.sleep(4)  # To view the result

driver.quit()
