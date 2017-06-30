from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by  import By
from selenium.webdriver.support  import expected_conditions as EC
import unittest
from selenium.webdriver.common.action_chains  import ActionChains
import time
from selenium.webdriver.common.keys  import Keys


class Test4(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()   
    
    def test_test4(self):
        time.sleep(5)
        FbLink = "//a[@class='wsite-social-item wsite-social-facebook']"    
        twLinkElement=WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(FbLink))                                 
        mainWindowHandle = driver.window_handles
        print "main Window handle: %s" %mainWindowHandle
        
        twLinkElement.click()
        allWindowsHandlesList = driver.window_handles
        print "all window handles list: %s" %allWindowsHandlesList
        
        for handle in allWindowsHandlesList:
            if handle != mainWindowHandle[0]:
                driver.switch_to.window(handle)
                break

        time.sleep(10)

        """
        FbUsernameElement=WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('email'))
        FbPasswordElement=WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('pass'))
        FbsignButton=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_css_selector("#loginbutton"))
        """
        #Alternative option
        
        FbUsernameElement=WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('email'))
        FbPasswordElement=WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('pass'))
        FbsignButton=WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_css_selector("#loginbutton"))
                                       
        FbUsernameElement.send_keys('jisan@gmail.com')
        FbPasswordElement.send_keys('Hello')
        FbsignButton.click() 
        
                      
    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
