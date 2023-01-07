import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com/giris/")
driver.maximize_window()

rememberButton = driver.find_element(By.ID, "rememberme")
time.sleep(3)
print(rememberButton.is_selected())
rememberButton.click()
time.sleep(3)
print(rememberButton.is_selected())

driver.quit()
