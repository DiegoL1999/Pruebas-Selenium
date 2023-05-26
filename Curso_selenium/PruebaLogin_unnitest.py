import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Prueba_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

        t = 2


    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom=driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas=driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn=driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("diego")
        pas.send_keys("123")
        btn.click()
        error=driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]")
        error=error.text
        if(error=="Epic sadface: Username and password do not match any user in this service"):
            print("el error de los es correcto")
            print("Prueba uno ok")
        time.sleep(.1)

    def test_login2(self):
            driver = self.driver
            driver.get("https://www.saucedemo.com/")
            self.driver.maximize_window()
            nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
            pas = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
            btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
            nom.send_keys("")
            pas.send_keys("123")
            btn.click()
            error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
            error = error.text
            print("falta el nombre")
            print("prueba2 ok")
            '''if (error == "Epic sadface: Username and password do not match any user in this service"):
                print("Los datos no son correctos")'''
            time.sleep(.1)
    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("diego")
        pas.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//div[@class='error-message-container error'][contains(.,'Epic sadface: Password is required')]")
        error = error.text
        if (error == "Epic sadface: Password is required"):
            print("Falta password")
            print("Prueba tres ok")
        time.sleep(.1)


    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        pas.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//div[@class='error-message-container error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        if (error == "Epic sadface: Username is required"):
            print("Faltan ambos")
            print("Prueba 4 pendiente")
        time.sleep(.1)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        pas = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        pas.send_keys("secret_sauce")
        btn.click()

        elemento = driver.find_element(By.XPATH, "//div[contains(@class,'app_logo')]")
        elemento.is_enabled()

        print("El elemento es "+str(elemento))

        time.sleep(.1)

    def tearDown(self):
        driver = self.driver
        driver.close()
