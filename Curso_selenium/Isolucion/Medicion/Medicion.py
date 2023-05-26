import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Isolucion.funciones import funciones_isolucion
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException

t= 3

class Creacion_Indicador(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")


    def test1(self):

        try:
            driver = self.driver
            f = funciones_isolucion(driver)
            f.Navegar("https://qa.isolucion.co/PaginaLogin.aspx", .1)
            f.texto_multiple("id", "UserText", "admin", .1)
            f.texto_multiple("id", "PasswordText", "12345", .1)
            f.click_multiple("id", "btnLogin", .1)

            medic = driver.find_element(By.XPATH, "//ul[@id='MenuUserUl']/li[6]/a[@href='#']")
            admini = driver.find_element(By.XPATH, "//ul[@id='MenuUserUl']/li[6]/ul[@class='dropdown-menu']/li[5]/div/div[2]")

            act = ActionChains(driver)
            act.move_to_element(medic).move_to_element(admini).click().perform()

            f.click_multiple("xpath","/html//div[@id='divMasterContenidoPrincipal']//div[@class='ng-scope']/div[1]/div[@class='col-xs-4 titleMenu']", .1)
            f.click_multiple("xpath", "//div[@class='col-xs-4 titleMenu'][contains(.,'Creación de indicadores')]", .1)
            f.click_multiple("xpath", "//a[contains(@id,'1')][@class='LinkPestania'][contains(.,'Nuevo')]", .1)
            f.click_multiple("xpath", "/html//input[@id='ContentPlaceHolder1_ctrSucursal_chbEsNivelGlobal']", .1)
            f.texto_multiple("xpath", "//input[contains(@id,'txtNomIndicador')]", "Indicador", .1)
            f.texto_multiple("xpath", "//textarea[contains(@id,'ContentPlaceHolder1_txtObjetivoEspecifico')]", "objetoEspecifico",.1)
            f.texto_multiple("xpath", "//textarea[contains(@id,'ContentPlaceHolder1_txtQuienAnaliza')]", "Fuente informacion", .1)
           # f.select_xpath_type("//select[contains(@id,'ContentPlaceHolder1_ddlTendencia')]", "Positiva", .1)
           # f.select_Xpath_test("//select[contains(@id,'ddlIndicadorTipo')]", "aseguramiento de calidad", .1)
           # f.select_Xpath_test("//select[contains(@id,'ContentPlaceHolder1_ddlIndicadorClase')]", "CLASE 2", .1)
           # f.check_Xpath("//input[contains(@id,'chbActivo')][@type='checkbox']", .1)
           # f.check_Xpath("//input[contains(@id,'chbNotificarNuevasMediciones')][@type='checkbox']", .1)
           # f.texto_xpath("//textarea[contains(@id,'ContentPlaceHolder1_txtFuenteInformacion')]", "Manual", .1)
           # f.texto_xpath("/html//input[@id='txtDecimalSignoMeta']", "1000", .1)
           # f.texto_xpath("/html//input[@id='txtDecimalSignoToleranciaSuperior']", "1000", .1)
          # f.texto_xpath("/html//input[@id='txtDecimalSignoToleranciaInferior']", "800", .1)
          #  f.texto_xpath("/html//textarea[@id='ContentPlaceHolder1_txtObservacionesIndicador']", "descripcion de los hechos", .1)
            f.check_CSS("input#ContentPlaceHolder1_chbActivo")
            f.select_xpath_type("xpath", "value", "//select[contains(@id,'ContentPlaceHolder1_ddlTendencia')]", "2", .1)
           # f.select_Xpath_test("//select[contains(@id,'ddlFrecuenciaMedicion')]", "Mensual", 1)
          #  f.select_Xpath_test("//select[contains(@id,'ContentPlaceHolder1_ddlSistemaG')]", "Actividades de control", .1)
         #   f.click_Xpath("//input[contains(@id,'ContentPlaceHolder1_imbFamiliaBusqueda')]", 30)
            #f.click_Xpath("//span[contains(.,'Nuevo registro')]", 30)
           # f.texto_xpath("//input[contains(@id,'txtNomFamilia')]", "qa", 30)
            #f.check_Xpath ("(//input[contains(@onchange,'modificarValores(this.value,this.checked);')])[10]", 10)
            f.click_multiple("xpath", "//input[contains(@id,'ContentPlaceHolder1_imbFamiliaBusqueda')]")
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//span[contains(@id,'ui-id-1')]")))
            f.click_multiple("xpath", "//input[contains(@id,'chk22')]")

        except TimeoutException as ex:
            print(ex.msg)
            print("Hay un problema para acceder a la ruta")