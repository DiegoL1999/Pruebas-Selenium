
import time

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

t = 1

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")


driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()
time.sleep(t)
#obteniendo links de la pagina
links=driver.find_element(By.TAG_NAME,"a")

print("El numero de link que hay en la es:", len(links))

for num in links:
  print(num.text)

driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Date pickers')])[1]")

time.sleep(t)
driver.close()