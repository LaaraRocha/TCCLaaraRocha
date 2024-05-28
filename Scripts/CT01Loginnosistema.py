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

class TestCT01Loginnosistema():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cT01Loginnosistema(self):
    self.driver.get("https://teste.areacentral.com.br/sistema/")
    self.driver.set_window_size(1552, 840)
    self.driver.find_element(By.ID, "USR_APELIDO").click()
    time.sleep(5)
    self.driver.find_element(By.ID, "USR_APELIDO").send_keys("financeiro.redeoeste")
    time.sleep(2)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".ui-p-2")
    assert len(elements) > 0
    time.sleep(2)
    self.driver.find_element(By.ID, "USR_SENHA").click()
    self.driver.find_element(By.ID, "USR_SENHA").send_keys("ABC")
    self.driver.find_element(By.ID, "btn-entrar").click()
    time.sleep(5)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".alert")
    assert len(elements) > 0
    time.sleep(2)
    self.driver.find_element(By.ID, "USR_SENHA").click()
    time.sleep(2)
    self.driver.find_element(By.ID, "USR_SENHA").send_keys("Ac@123456")
    self.driver.find_element(By.ID, "form-login").click()
    self.driver.find_element(By.CSS_SELECTOR, "#btn-entrar > span").click()
    time.sleep(5)
  