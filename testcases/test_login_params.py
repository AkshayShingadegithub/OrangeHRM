import time

import pytest

from PageObjects.LoginPage import loginpage
from Utilities.Logger import LogGenerator
from Utilities.Readproperties import Readconfig


class Test_login_params:

    url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.Mark.regression
    def test_login_params_003(self, setup,getdataforlogin):
        self.driver = setup
        self.log.info("test_login_params_003 is started")
        self.log.info("browser is opening")
        self.driver.get(self.url)
        self.lp = loginpage(self.driver)
        self.log.info("Entering username-->" + getdataforlogin[0])
        self.lp.enter_username(getdataforlogin[0])
        self.log.info("Entering password-->" + getdataforlogin[1])
        self.lp.enter_password(getdataforlogin[1])
        self.log.info("Click login")
        self.lp.Click_login()
        time.sleep(2)

        login_status_list = []

        if self.lp.login_status() == True:
            if getdataforlogin[2] == "Pass":
                login_status_list.append("Pass")
                self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_params_003-Pass.png")
                self.log.info("Click MenuButton")
                self.lp.Click_MenuButton()
                self.log.info("Click Logout")
                self.lp.Click_Logout()
            elif getdataforlogin[2] == "Fail":
                login_status_list.append("Fail")
                self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_params_003-Fail.png")
        else:
            if getdataforlogin[2] == "Pass":
                login_status_list.append("Fail")
                self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_params_003-Fail.png")
            elif getdataforlogin[2] == "Fail":
                login_status_list.append("Pass")
                self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_params_003-Pass.png")

        print(login_status_list)
        if "Pass" in login_status_list:
            self.log.info("test_login_params_003 is Passed")
            assert True
        else:
            self.log.info("test_login_params_003 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_params_003 is Completed")