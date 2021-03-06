from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time


class Test1(unittest.TestCase):

    def __init__(self,*args):
        super().__init__(*args)
        self.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        #self.driver.implicitly_wait(30)
        self.base_url = "###################"


    def setUp(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.username = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//input[@type='text']"))
        self.username.click()
        self.username.send_keys("Luke")

        self.password = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//input[@type='password']"))
        self.password.click()
        self.password.send_keys("Skywalker")

        self.login = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='login-form']/fieldset/button"))
        self.login.click()

        time.sleep(6)

    def test_createuser(self):
        self.createuser = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_id("bAdd"))
        self.createuser.click()

        self.firstname = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.firstName']"))
        self.firstname.click()
        self.firstname.send_keys("Mohsin")

        self.secondname = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.lastName']"))
        self.secondname.click()
        self.secondname.send_keys("Chowdhury")

        self.startdate = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.startDate']"))
        self.startdate.click()
        self.startdate.send_keys("2019-12-06")

        self.email = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.email']"))
        self.email.click()
        self.email.send_keys("chy.mohsin@gmail.com")

        self.adduser = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_class_name("formFooter"))
        self.adduser.click()

        time.sleep(6)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
###################################################################################################################################
    from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time


class Test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        cls.driver.implicitly_wait(30)
        cls.base_url = "##############################################################################"
        cls.driver.get(cls.base_url)
        cls.driver.maximize_window()

    def test_login(self):
        self.username = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//input[@type='text']"))
        self.username.click()
        self.username.send_keys("Luke")

        self.password = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//input[@type='password']"))
        self.password.click()
        self.password.send_keys("Skywalker")

        self.login = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='login-form']/fieldset/button"))
        self.login.click()

        time.sleep(6)

    def test_createuser(self):
        self.createuser = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_id("bAdd"))
        self.createuser.click()

        self.firstname = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.firstName']"))
        self.firstname.click()
        self.firstname.send_keys("Mohammad Mohsin")

        self.secondname = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.lastName']"))
        self.secondname.click()
        self.secondname.send_keys("Chowdhury")

        self.startdate = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.startDate']"))
        self.startdate.click()
        self.startdate.send_keys("2019-12-06")

        self.email = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.email']"))
        self.email.click()
        self.email.send_keys("chy.mohsin@gmail.com")

        self.adduser = WebDriverWait(self.driver, 10). \
            until(lambda driver: driver.find_element_by_class_name("formFooter"))
        self.adduser.click()

        time.sleep(6)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
#########################################################################################################################
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

import unittest

import time


class Test1(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get("#####")
        driver.maximize_window()
        username = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//input[@type='text']"))
        username.click()
        username.send_keys("Luke")

        password = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//input[@type='password']"))
        password.click()
        password.send_keys("Skywalker")

        login = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[@id='login-form']/fieldset/button"))
        login.click()

        time.sleep(6)



    def test_createuser(self):
        
        createuser = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_id("bAdd"))
        createuser.click()

        firstname=WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.firstName']"))
        firstname.click()
        firstname.send_keys("Mohammad Mohsin")

        secondname=WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.lastName']"))
        secondname.click()
        secondname.send_keys("Chowdhury")

        startdate = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.startDate']"))
        startdate.click()
        startdate.send_keys("2019-12-06")

        email = WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_xpath("//*[input/@ng-model='selectedEmployee.email']"))
        email.click()
        email.send_keys("chy.mohsin@gmail.com")

        adduser= WebDriverWait(driver, 10). \
            until(lambda driver: driver.find_element_by_class_name("formFooter"))
        adduser.click()

        time.sleep(6)

    def tearDown(self):
        driver.quit()


if __name__ == "__main__":
    unittest.main()
