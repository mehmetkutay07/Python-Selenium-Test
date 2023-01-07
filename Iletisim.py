import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com")
driver.maximize_window()


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "İletişim").click()
time.sleep(2)
driver.find_element(By.ID, "wpforms-1085-field_0").send_keys("Mehmet Kutay")
time.sleep(2)
driver.find_element(By.ID, "wpforms-1085-field_0-last").send_keys("Dündar")
time.sleep(2)
driver.find_element(By.ID, "wpforms-1085-field_1").send_keys("kdundar2000windowslive.com")
time.sleep(2)
driver.find_element(By.ID, "wpforms-1085-field_2").send_keys("test message")
time.sleep(2)
driver.find_element(By.ID, "wpforms-submit-1085").click()

message = driver.find_element(By.ID, "wpforms-1085-field_1-error").text
if "Geçerli bir e-posta girin." in message:
    print("Wrong Email Type")
else:
    print("True Email Type")

driver.quit()


