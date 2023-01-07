import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com/xiaomi-amazfit-pace-2-stratos-akilli-saat/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,5000);")
time.sleep(3)
facebookButton = driver.find_element(By.LINK_TEXT, "Facebook")
print(facebookButton.is_enabled())
TwitterButton = driver.find_element(By.LINK_TEXT, "Twitter")
print(TwitterButton.is_enabled())
PinterestButton = driver.find_element(By.LINK_TEXT, "Pinterest")
print(PinterestButton.is_enabled())
LinkedinButton = driver.find_element(By.LINK_TEXT, "LinkedIn")
print(LinkedinButton.is_enabled())
TumblrButton = driver.find_element(By.LINK_TEXT, "Tumblr")
print(TumblrButton.is_enabled())
WhatsappButton = driver.find_element(By.LINK_TEXT, "WhatsApp")
print(WhatsappButton.is_enabled())

driver.quit()







