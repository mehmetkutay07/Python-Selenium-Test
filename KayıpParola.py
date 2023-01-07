import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com/kayipparola/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.ID, "user_login").send_keys("test123")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "tml-button").click()
time.sleep(2)
header = driver.current_url
if "https://teknomain.com/kayipparola/wp-login.php?checkemail=confirm" in header:
    print("Error:The page is not working.")

driver.quit()
