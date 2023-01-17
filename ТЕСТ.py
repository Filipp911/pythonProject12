import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://sovcombank.ru")
items = driver.find_elements_by_xpath("//div[@class='group']")
items[0].click()