import logging
import socket
import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time

class Test_001_DDT_login:
    baseurl= Readconfig.getApplicationurl()
    path=".//TestData//LogData.xlsx"

    logger=LogGen.loggen()


    def test_login(self,setup):
        self.logger.info("----------Start___test_login_____")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)

        self.driver.implicitly_wait(20)
        self.row=XLUtils.getRowCount(self.path,'Sheet1')
        print("nos of rows ",self.row)
        lst_status = []

        for r in range(2,self.row+1):
            self.user =XLUtils.readData(self.path,'Sheet1',r,1)
            self.pwd = XLUtils.readData(self.path, 'Sheet1', r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r,3)


            self.lp.setusername(self.user)
            self.lp.setpassword(self.pwd)
            self.lp.clickloginbutton()
            time.sleep(4)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title ==exp_title:
                if self.exp=='Pass':
                    self.logger.info("-----TestCase Passed------")
                    lst_status.append("Pass")
                    self.lp.clicklogoutlink()
                elif self.exp=='Fail':
                    self.logger.info("-----TestCase Failed------")
                    lst_status.append("Fail")
                    self.lp.clicklogoutlink()
            elif act_title !=exp_title:
                if self.exp=='Pass':
                    self.logger.info("-----TestCase Failed------")
                    lst_status.append("Fail")
                elif self.exp=='Fail':
                    self.logger.info("-----TestCase Passed------")
                    lst_status.append("Pass")


        if "Fail" not in lst_status:
           self.logger.info("DDT Test is Passed")
           self.driver.close()
           assert True
        else:
            self.logger.info("DDT Test is Failed")
            self.driver.close()
            assert False


        self.logger.info("---End of Test_Login_ddt---")