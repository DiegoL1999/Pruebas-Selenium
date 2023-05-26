
import time

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

t = 10

driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")


driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()



try:
 caja1 = driver.find_element(By.XPATH, "//input[contains(@id,'firstName')]")
 caja1.send_keys("Diego" + Keys.TAB + "Andres" + Keys.TAB + "dloaizaurdaneta@gmail.com")
 btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#genterWrapper > .col-md-9.col-sm-12 > div:nth-of-type(2) > label")))
 btn1.click()
 caja2 = driver.find_element(By.XPATH, "//input[contains(@id,'userNumber')]")
 caja2.send_keys("3023907009" + Keys.TAB + Keys.ENTER)
 btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#hobbiesWrapper > .col-md-9.col-sm-12 > div:nth-of-type(2) > label")))
 btn2.click()
 time.sleep(t)
 btn3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//input[contains(@class,'form-control-file')]"))
 btn3 = driver.find_element(By.XPATH, "//input[contains(@class,'form-control-file')]")
 btn3.send_keys("C://Users//ivern//OneDrive//Imágenes//prueba.jpg")
 time.sleep(t)


except:

 print("No se pudo realizar la prueba")

finally:

 print("intentelo nuevamente")

driver.close()

