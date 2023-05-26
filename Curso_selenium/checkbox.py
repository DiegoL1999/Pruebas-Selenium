
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
t=3

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rct-checkbox")))
btn1.click()

time.sleep(t)

driver.close()

