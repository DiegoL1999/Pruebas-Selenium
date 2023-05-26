import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")

#driver.switch_to_alert().accept()

#driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
#time.sleep(4)


#driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
#time.sleep(t)

#driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()
#time.sleep(4)

#driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Close')])[1]")
#driver.close()

driver.find_element(By.XPATH, "//a[@href='#myModal0']").click()

try:
    buscar = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]" )))
    buscar = driver.find_element(By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    time.sleep(5)

except TimeoutException as ex:
  print(ex.msg)
  print("El elemento no esta disponible")


time.sleep(4)
