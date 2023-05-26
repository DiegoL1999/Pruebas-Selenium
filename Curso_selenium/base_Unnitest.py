import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.maximize_window()
        t = 2


    def test1(self):
        driver = self.driver
        driver.get("")

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__name__':
    unittest.main()