
import time

import pytest

from PageObjects.LoginPage import loginpage
from Utilities.Logger import LogGenerator
from Utilities.Readproperties import Readconfig


class Testlogin:

    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.Mark.sanity
    def test_Url_001(self,setup):
        self.driver = setup
        self.log.info("test_Url_001 is started")
        self.log.info("browser is opening")
        self.driver.get(self.url)
        print(self.driver.title)
        time.sleep(2)
        if self.driver.title == "OrangeHRM":
            self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_Url_001-Pass.png")
            self.log.info("test_Url_001 is Passed")
        else:
            self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_Url_001-Fail.png")
            self.log.info("test_Url_001 is Failed")

        self.log.info("test_Url_001 is completed")

    @pytest.Mark.sanity
    def test_login_002(self,setup):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("browser is opening")
        self.driver.get(self.url)
        self.lp = loginpage(self.driver)
        self.log.info("Entering username-->" + self.username)
        self.lp.enter_username(self.username)
        self.log.info("Entering password-->" + self.password)
        self.lp.enter_password(self.password)
        self.log.info("Click login")
        self.lp.Click_login()

        if self.lp.login_status() == True:
            time.sleep(2)
            self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_002-Pass.png")
            self.log.info("Click MenuButton")
            self.lp.Click_MenuButton()
            self.log.info("Click Logout")
            self.lp.Click_Logout()
            self.log.info("test_login_002 is Passed")
            assert True
        else:
            self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_002-Fail.png")
            self.log.info("test_login_002 is Failed")
            assert False

        self.log.info("test_login_002 is Completed")





