import pytest
from selenium import webdriver
from PageObject.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


class Test_001_login:
    baseurl= Readconfig.getApplicationurl()
    username= Readconfig.getusername()
    password= Readconfig.getpassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("----------Start___Test__001___login_____")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        act_title=self.driver.title
        if act_title=="Your store. Login":
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            assert False
        self.logger.info("----------End___Test__001___login_____")


    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("----------Start___test_login_____")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.driver.implicitly_wait(20)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickloginbutton()
        act_title=self.driver.title


        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("----------End___test_login_____")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("----------End___test_login_____")
            assert False

