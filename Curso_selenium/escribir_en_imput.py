import time

from selenium import webdriver
from selenium.webdriver.common.by import By



#from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Diego")
time.sleep(1)

ema = driver.find_element(By.XPATH, "//input[contains(@id,'userEmail')]").send_keys("dloaizaurdaneta@gmail.com")
time.sleep(1)

cur = driver.find_element(By.XPATH, "//textarea[contains(@id,'currentAddress')]").send_keys("345")
time.sleep(1)

pa = driver.find_element(By.XPATH, "//textarea[contains(@id,'permanentAddress')]").send_keys("345")
time.sleep(2)

driver.close()

