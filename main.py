import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://google.ru")
textfield = driver.find_element_by_xpath("//input[@name='q']")
textfield.send_keys("Совкомбанк")
submit_button = driver.find_element_by_xpath("//div[@jsname='VlcLAe']//input[@class='gNO89b']")
time.sleep(1)
submit_button.click()
driver.get("https://sovcombank.ru")





#driver.quit()