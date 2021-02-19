from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

import unittest

import time


from selenium import webdriver

class WidgetArea():

  def setUp(self):
    self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    self.driver.implicitly_wait(30)
    self.driver.maximize_window()
    self.driver.get("http://demoqa.com/")

  def tearDown(self):
    self.driver.quit()

  def widget_area(self):
    elements = self.driver.find_elements_by_xpath("//div[@id='secondary']/aside")
    try:
        assert len(elements) == 4
        print("Test pass")
    except AssertionError:
        print("Assertion failed")

  def widget_list(self):
    elements = self.driver.find_elements_by_xpath("//ul[@id='menu-widget']/li")
    try:
        assert len(elements) == 7
        print("Test pass")
    except AssertionError:
        print("Assertion failed")

  def interaction(self):
    elements = self.driver.find_elements_by_xpath("//ul[@id='menu-interactions']/li")
    try:
        assert len(elements) == 5
        print("Test pass")
    except AssertionError:
        print("Assertion failed")

  def main(self):
    self.setUp()
    self.widget_area()
    self.widget_list()
    self.interaction()
    self.tearDown()


if __name__ == '__main__':
    new = WidgetArea()
    new.main()
