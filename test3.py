from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by  import By
from selenium.webdriver.support  import expected_conditions as EC
import unittest
from selenium.webdriver.common.action_chains  import ActionChains
import time
from selenium.webdriver.common.keys  import Keys


class Test3(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()   
    
    def test_test3(self):        
        dropdownvalue= "select#wsite-com-product-option-Quantity option[value='3']"
        x = WebDriverWait(driver, 10).\
                               until(lambda driver:driver.find_element_by_css_selector(dropdownvalue))
        x.click()
        time.sleep(10)
            
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
