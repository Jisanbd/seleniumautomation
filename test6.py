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
    
    def test_test6(self):
        #Click on search field
        #implicit waits
        #x = driver.find_element_by_xpath("//input[@name='q']")
        #x = driver.find_element_by_css_selector("input[name=q]")
        #x = driver.find_element_by_name("q")
        #x = driver.find_element_by_class_name("wsite-search-input")
        
        #explicit wait
        x = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='q']"))
        #x = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector(""))
        #x = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(""))
        #x = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name(""))
        x.click()
        time.sleep(10)
                      
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
