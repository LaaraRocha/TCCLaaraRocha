# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCT07Pontosdousuario():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cT07Pontosdousuario(self):
    self.driver.get("https://teste.areacentral.com.br/sistema/")
    self.driver.set_window_size(1552, 840)
    time.sleep(2)
    self.driver.find_element(By.ID, "USR_APELIDO").click()
    self.driver.find_element(By.ID, "USR_APELIDO").send_keys("financeiro.redeoeste")
    self.driver.find_element(By.ID, "USR_SENHA").click()
    self.driver.find_element(By.ID, "USR_SENHA").send_keys("Ac@123456")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#btn-entrar > span").click()
    time.sleep(2)
    elements = self.driver.find_elements(By.LINK_TEXT, "Ver Todas as Pontuações")
    assert len(elements) > 0
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "Ver Todas as Pontuações").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) .dropdown").click()
    self.driver.find_element(By.LINK_TEXT, "Adicionar pontos").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-lg:nth-child(2)").click()
    time.sleep(2)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".msgbox-wrapper")
    assert len(elements) > 0
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success:nth-child(1)").click()
    time.sleep(2)
    self.driver.find_element(By.NAME, "observacao").click()
    self.driver.find_element(By.NAME, "observacao").send_keys("Adicionar pontos")
    time.sleep(2)
    self.driver.find_element(By.NAME, "pontuacao").click()
    self.driver.find_element(By.NAME, "pontuacao").send_keys("5")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-lg:nth-child(2)").click()
    time.sleep(2)
  
