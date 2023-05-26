import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://demoqa.com/")

titulo=driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
btn1 = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")

if(titulo.is_displayed()==True):
    print("Existe la imegen")
    btn1.click()
    time.sleep(2)
else:
    print("No existe la imagen")
time.sleep(2)
driver.close()