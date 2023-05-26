import time

from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()
#driver.implicitly_wait(10)
t=3


driver.find_element(By.XPATH,"//input[contains(@id,'user-message')]").send_keys("prueba")

time.sleep(t)

driver.close()

