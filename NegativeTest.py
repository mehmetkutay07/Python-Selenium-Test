import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com/giris/")
driver.maximize_window()

# (Negative Test For Login Page)
driver.find_element(By.ID, "user_login").send_keys("deneme123")
time.sleep(2)
driver.find_element(By.ID, "user_pass").send_keys("sifre123")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "tml-button").click()
message = driver.find_element(By.CLASS_NAME, "tml-error").text
assert "ERROR: The username or password you entered is incorrect. Lost your password?" in message

