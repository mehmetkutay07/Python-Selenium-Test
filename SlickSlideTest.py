import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://teknomain.com/")
driver.maximize_window()

driver.find_element(By.ID, "slick-slide-control00").click()
time.sleep(3)
driver.find_element(By.ID, "slick-slide-control01").click()
time.sleep(3)
driver.find_element(By.ID, "slick-slide-control02").click()
time.sleep(3)
driver.find_element(By.ID, "slick-slide-control03").click()
time.sleep(3)
driver.find_element(By.ID, "slick-slide-control04").click()
time.sleep(3)





