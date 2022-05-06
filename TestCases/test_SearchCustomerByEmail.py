import logging

import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerPage import AddCustomerPage
from PageObject.SearchCustomer import SearchCustomer

from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
import time

class Test_SearchCustomerByEmil:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()

    def test_SearchCustomerByEmil(self,setup):
        self.logger.info("----------Start___test_SearchCustomerByEmil_____")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.lp=LoginPage(self.driver)
        print(self.username)
        self.lp.setusername(self.username)
        print(self.password)
        self.lp.setpassword(self.password)
        self.lp.clickloginbutton()
        self.logger.info("----------login Successful_____")

        self.logger.info("----------Starting___Search Customer By Emil_____")
        self.driver.implicitly_wait(20)
        self.addcust=AddCustomerPage(self.driver)
        self.addcust.clickonCustomerMenu()
        time.sleep(2)
        self.addcust.clickonCustomerMenuitem()

        self.searchcust=SearchCustomer(self.driver)
        self.searchcust.setemail("victoria_victoria@nopCommerce.com")
        self.searchcust.clickSearchBtn()
        time.sleep(5)

        status=self.searchcust.getCustomerEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("----------Ending___Search Customer By Emil_____")
        self.logger.info("----------End___test_SearchCustomerByEmil_____")

