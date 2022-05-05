import logging
import random
import string
import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from PageObject.AddCustomerPage import AddCustomerPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class Test_AddCustomer:
    baseurl = Readconfig.getApplicationurl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_AddCustomer(self,setup):
        self.logger.info("----------Start___test_AddCustomer_____")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickloginbutton()
        self.logger.info("----------login Successful_____")
        self.logger.info("----------starting AddCustomer_____")
        time.sleep(15)
        self.addcust=AddCustomerPage(self.driver)
        self.addcust.clickonCustomerMenu()
        time.sleep(3)
        self.addcust.clickonCustomerMenuitem()

        self.addcust.clickOnAddnew()
        self.logger.info("----------Providing Customer info_____")

        self.email =random_generator()+"@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('test@123')
        self.addcust.setFirstName('Dhananjay')
        self.addcust.setLastName('Kumar')
        self.addcust.setdob('7/05/1985')
        self.addcust.setCompanyName('busyQA')
        time.sleep(2)
        self.addcust.setManageofVendor(2)
        time.sleep(2)
        self.addcust.setGender("Male")
        self.addcust.setAdmincontent("This is for testing.........")
        time.sleep(2)
        #self.addcust.setCustomerRole('Guest')


        self.addcust.ClickSave()

        self.logger.info("-------Saving customer info--------")

        self.logger.info("-------Add customer validation started---------")
        self.msg=self.driver.find_element_by_tag_name('body').text
        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("-------Testcase Add customer Passed---------")
        else:
            self.logger.info("-------Testcase Add customer Passed---------")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Add customer_scr.png")
            assert False

        self.logger.info("-------Add customer validation End---------")
        self.driver.close()


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))