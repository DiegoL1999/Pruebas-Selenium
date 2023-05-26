
import time

from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
t = .3

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()

try:
    prinom = driver.find_element(By.XPATH, "//input[@name='first_name']")
    prinom.send_keys("Diego")
    prinom.send_keys(Keys.TAB + "andres" + Keys.TAB + "dloaizaurdaneta@gmail.com" + Keys.TAB+"3023907009" + Keys.TAB + "Calle 30 #20-25" + Keys.TAB + "Bogota" + Keys.TAB)
    stateSelect = driver.find_element(By.CSS_SELECTOR, "select.form-control")
    state = Select(stateSelect)
    state.select_by_visible_text("Alabama")
    zcode = driver.find_element(By.XPATH, "//input[@name='zip']")
    zcode.send_keys("46886486")
    zcode.send_keys(Keys.TAB + "https://demo.seleniumeasy.com/input-form-demo.html")
    btn1 = driver.find_element(By.XPATH, "//input[@value='yes']")
    btn1.click()
    text = driver.find_element(By.XPATH, "//textarea[@class='form-control']")
    text.send_keys("prueba QA 1 curso selenium" + Keys.TAB + Keys.ENTER)
    scroll = driver.find_element(By, "//textarea[@class='form-control']")
    ir = driver.execute_script("arguments[0].scrollIntoView();", scroll)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")
    time.sleep(t)

driver.close()

