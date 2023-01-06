import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com")
driver.maximize_window()

driver.find_element(By.ID, "menu-item-3930").click()
time.sleep(2)
driver.find_element(By.ID, "onesignal-slidedown-cancel-button").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "logo_small_wrapper").click()
time.sleep(2)
driver.quit()
