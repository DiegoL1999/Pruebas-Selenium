import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Isolucion.funciones import funciones_isolucion
from selenium.webdriver.chrome.service import Service


class Pagina_login(unittest.TestCase):

    def setUp(self):
        s = Service('C://drivers//chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test1(self):
        driver = self.driver
        f = funciones_isolucion(driver)
        f.Navegar("https://qa.isolucion.co/PaginaLogin.aspx", .1)
        f.texto_ID("UserText", "Diego", .1)
        f.texto_ID("PasswordText", "12345", .1)
        f.click_ID("btnLogin", .1)
        error = self.driver.find_element(By.CSS_SELECTOR, ".toast-message")
        error = error.text

        if (error == "No tiene acceso al Directorio Activo o no se encuentra el usuario. Error:"):
            print("Usuario no valido - Prueba exitosa")

    def test2(self):
        driver = self.driver
        f = funciones_isolucion(driver)
        f.Navegar("https://qa.isolucion.co/PaginaLogin.aspx", .1)
        f.texto_ID("UserText", "Admin", .1)
        f.texto_ID("PasswordText", "", .1)
        f.click_ID("btnLogin", .1)
        error = self.driver.find_element(By.CSS_SELECTOR, "div#PasswordText-error")
        error = error.text

        if (error == "Este campo es requerido"):
            print("Obligatoriedad del campo contraseña validado con exito")

    def test3(self):
        driver = self.driver
        f = funciones_isolucion(driver)
        f.Navegar("https://qa.isolucion.co/PaginaLogin.aspx", .1)
        f.texto_ID("UserText", "", .1)
        f.texto_ID("PasswordText", "12345", .1)
        f.click_ID("btnLogin", .1)
        error = self.driver.find_element(By.CSS_SELECTOR, "div#UserText-error")
        error = error.text

        if (error == "Este campo es requerido"):
            print("Obligatoriedad del campo usuario validado con exito")

    def test4(self):
        driver = self.driver
        f = funciones_isolucion(driver)
        f.Navegar("https://qa.isolucion.co/PaginaLogin.aspx", .1)
        f.texto_ID("UserText", "Admin", .1)
        f.texto_ID("PasswordText", "123", .1)
        f.click_ID("btnLogin", .1)
        error = self.driver.find_element(By.CSS_SELECTOR, ".toast-message")
        error = error.text

        if (error == "No tiene acceso al Directorio Activo o no se encuentra el usuario. Error:"):
            print("clave no valida - prueba realizada con exito")

    def test5(self):
        driver = self.driver
        f = funciones_isolucion(driver)
        f.Navegar("https://qa.isolucion.co/PaginaLogin.aspx", .1)
        f.texto_ID("UserText", "Administrador", .1)
        f.texto_ID("PasswordText", "12345", .1)
        f.click_ID("btnLogin", .1)

        logo = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img#LogoApp")))
        logo.is_displayed()
        print("Sesion iniciada con exito")
