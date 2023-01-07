import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://teknomain.com/xiaomi-amazfit-pace-2-stratos-akilli-saat/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,7200);")
time.sleep(3)
Comment = driver.find_element(By.ID, "comment")
print(Comment.is_enabled())
Author = driver.find_element(By.ID, "author")
print(Author.is_enabled())
Email = driver.find_element(By.ID, "email")
print(Email.is_enabled())
Website = driver.find_element(By.ID, "url")
print(Website.is_enabled())
cookiesBox = driver.find_element(By.ID, "wp-comment-cookies-consent")
print(cookiesBox.is_selected())
cookiesBox.click()
time.sleep(3)
print(cookiesBox.is_selected())
submitButton = driver.find_element(By.ID, "submit")
print(submitButton.is_enabled())

driver.quit()