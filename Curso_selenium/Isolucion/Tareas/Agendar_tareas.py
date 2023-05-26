import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Isolucion.funciones import funciones_isolucion
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class Creacion_Indicador(unittest.TestCase):

    def setUp(self):
        s = Service('C:/drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test1(self):

        try:
            driver = self.driver
            f = funciones_isolucion(driver)
            f.Navegar("https://qa.isolucion.co/PaginaLogin.aspx", .1)
            f.texto_multiple("id", "UserText", "Admin")
            f.texto_multiple("xpath", "//input[@id='PasswordText']", "12345")
            f.click_multiple("id", "btnLogin")

            tar = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle'][contains(.,'Tareas')]")
            atar = driver.find_element(By.XPATH, "(//div[contains(.,'Agendar tareas')])[5]")

            act = ActionChains(driver)
            act.move_to_element(tar).move_to_element(atar).click().perform()


            #f.select_xpath_type("xpath", "//select[contains(@id,'ContentPlaceHolder1_ddlTipoTarea')]", "Indicadores", 1)
            f.texto_multiple("xpath", "//input[contains(@id,'ContentPlaceHolder1_txtNomTarea')]", "tarea prueba")
           # f.texto_xpath("//input[contains(@id,'ContentPlaceHolder1_txtNomTarea')]", "TaraDePrueba", 1)
            f.texto_multiple("xpath", "//textarea[contains(@id,'ContentPlaceHolder1_txtDescripcion')]", "Descripcion")
           # f.click_Xpath("//input[contains(@id,'ContentPlaceHolder1_imbBuscarDocumento')]", 1)
           # f.prueba("(//input[contains(@class,'CajaTexto')])[2]", 1)
           # f.click_Xpath("(//a[@class='ItemPrincipalGrilla'])[5]", 35)
            #cli = driver.find_element(By.XPATH, "//a[@class='ItemPrincipalGrilla'][contains(.,'jenny11145645_v456')]")
            #act.move_to_element(cli).move_to_element().click().perform()
           # f.click_Xpath("/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/table[1]/tbody[1]/tr[9]/td[1]/a[1]", 35)
           # f.check_Xpath("//input[@id='chk2']", 1)
            # f.click_Xpath("//input[contains(@id,'MainContentPlaceHolder_btnGrabar')]", 1)
           # f.click_Xpath('//*[@id="List"]/tbody/tr[3]/td/div/table/tbody/tr[5]/td[1]/a', 1)
            f.check_multiple("xpath", "//input[contains(@id,'chkRequiereRespuesta')]")
            f.click_multiple("id", "ContentPlaceHolder1_imbBuscarUsuario")
            f.clic_XY("xpath", "//input[contains(@id,'MainContentPlaceHolder_ctrBuscadorAZ_imbPaginaAdelante')]", 400, 200)

        except TimeoutException as ex:
            print(ex.msg)
            print("Hay un problema para acceder a la ruta")