import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.CLASS_NAME, "menu_mobile_icons").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "search_btn").send_keys("espor")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "button").click()
time.sleep(2)
driver.quit()
