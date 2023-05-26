import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")

btn = driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]")
btn.click()
time.sleep(2)

name_val= driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your first name')]")
name=name_val.text
#print("El valor del error es: "+name)
if(name=="Please supply your first name"):
    print("nombre asignado con exito")
    cn=driver.find_element(By.XPATH,"//input[contains(@name,'first_name')]")
    cn.send_keys("Diego")
else:
    print("Por favor introduzca el nombre")
time.sleep(2)

ap_val= driver.find_element(By.XPATH, "//small[@class='help-block'][contains(.,'Please supply your last name')]")
ap1=ap_val.text
#print("El valor del error es: "+name)
if(ap1=="Please supply your last name"):
    print("apellido asignado con exito")
    cn=driver.find_element(By.XPATH,"//input[contains(@name,'last_name')]")
    cn.send_keys("Loaiza")
else:
    print("Por favor introduzca el apellido")

print(btn.is_enabled())
if(btn.is_enabled()==False):
    print("Faltan campos por llenar")
else:
    print("Todo ok")
time.sleep(2)
driver.close()