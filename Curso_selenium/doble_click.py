import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Isolucion.funciones import funciones_isolucion

class doble_click(unittest.TestCase):

    def setUp(self):
        s = Service('C:/drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test1(self):

        try:
            driver = self.driver
            f = funciones_isolucion(driver)
            f.Navegar("https://demoqa.com/buttons", 2)
            f.Mouse_doble("id", "doubleClickBtn")


        except TimeoutException as ex:
            print(ex.msg)
            print("Hay un problema para acceder a la ruta")
