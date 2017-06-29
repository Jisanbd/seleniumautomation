from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by  import By

import unittest

import time


class Test1(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("http://travelingtony.weebly.com")
        driver.maximize_window()   
    
    def test_1(self):
        x=WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_xpath("//a[.='Contact']"))
        x.click()

        y=WebDriverWait(driver, 10).\
                             until(lambda driver: driver.find_element_by_xpath("//input[contains(@name, '_u303669969104487737[first]')]"))
        y.send_keys("maks")
        time.sleep(6)
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
