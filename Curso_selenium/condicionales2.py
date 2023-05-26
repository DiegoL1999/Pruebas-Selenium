import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://demoqa.com/text-box")

btn1 = driver.find_element(By.XPATH, "//div[contains(@class,'col-12 mt-4 col-md-3')]")
print(btn1.is_enabled())

if(btn1.is_enabled()==True):
    print("Puedes dar click")
else:
    print("No puedes dar clic")

time.sleep(1)
driver.close()