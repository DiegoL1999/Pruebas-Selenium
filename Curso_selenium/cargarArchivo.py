
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


#from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
t=5

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()

try:
    btn1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#fileinput")))
    btn1 = driver.find_element(By.CSS_SELECTOR, "input#fileinput")
    btn1.send_keys("C://Users//ivern//OneDrive//Imágenes//mi telefono//prueba.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")


driver.close()

