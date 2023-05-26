
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
time=4

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()

try:
    diasSelect = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select.form-control")))
    ds = Select(diasSelect)

    ds.select_by_index(3)


except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

    ciudad = Select(driver.find_element(By.CSS_SELECTOR, "select#multi-select"))
    time.sleep(time)
    ciudad.select_by_index(1)
    ciudad.select_by_index(3)
    ciudad.select_by_index(5)

    time.sleep(time)


driver.close()

