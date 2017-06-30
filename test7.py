from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by  import By
from selenium.webdriver.support  import expected_conditions as EC
import unittest
from selenium.webdriver.common.action_chains  import ActionChains
import time
from selenium.webdriver.common.keys  import Keys


class Test6(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("http://travelingtony.weebly.com")
        driver.maximize_window()   
    
    def test_test7(self):
        #x      = driver.find_elements_by_xpath("//img")
        #x      = driver.find_elements_by_css_selector("img")
        x      = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath("//img"))
        #x      = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_css_selector("img"))
        print x
        #time.sleep(10)
                      
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
