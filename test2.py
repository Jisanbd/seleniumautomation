from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by  import By
from selenium.webdriver.support  import expected_conditions as EC
import unittest
from selenium.webdriver.common.action_chains  import ActionChains
import time
from selenium.webdriver.common.keys  import Keys


class Test2(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("http://travelingtony.weebly.com")
        driver.maximize_window()   
    
    def test_test2(self):
        x = WebDriverWait(driver, 10).\
                               until(lambda driver: driver.find_element_by_name("q"))
        
        
        """
        x.click()
        x.send_keys("Leatherback")
        x.send_keys(Keys.ENTER) 
        """
        #Alternative method
        actions = ActionChains(driver)
        actions.send_keys_to_element(x, "Leatherback")
        actions.send_keys_to_element(x, Keys.ENTER)
        actions.perform()
        
        WebDriverWait(driver, 20).\
            until(lambda driver: driver.find_element_by_xpath("//span[@title='Leatherback Turtle Picture']"))
        
    
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
