import time

import pytest

from PageObjects.LoginPage import loginpage
from Utilities import XLutils
from Utilities.Logger import LogGenerator
from Utilities.Readproperties import Readconfig


class Test_login_ddt:

    url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "D:\\Pytest rev\\orangeHRM scratch\\testcases\\Testdata\\LoginTestData.xlsx"

    @pytest.Mark.regression
    def test_login_ddt_004(self, setup):
        self.driver = setup
        self.log.info("test_login_ddt_004 is started")
        self.log.info("browser is opening")
        self.driver.get(self.url)
        self.lp = loginpage(self.driver)
        self.rows = XLutils.getrowcount(self.path, 'Sheet1')
        print("No of rows are-->", self.rows)
        for r in range(2, self.rows+1):
            self.username = XLutils.readdata(self.path, 'Sheet1', r, 1)
            self.password = XLutils.readdata(self.path, 'Sheet1', r, 2)
            self.exp_status = XLutils.readdata(self.path, 'Sheet1', r, 3)
            self.log.info("Entering username-->" + self.username)
            self.lp.enter_username(self.username)
            self.log.info("Entering password-->" + self.password)
            self.lp.enter_password(self.password)
            self.log.info("Click login")
            self.lp.Click_login()
            time.sleep(2)
            login_status_list = []
            if self.lp.login_status() == True:
                if self.exp_status == "Pass":
                    login_status_list.append("Pass")
                    self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_ddt_004-Pass.png")
                    self.log.info("Click MenuButton")
                    self.lp.Click_MenuButton()
                    self.log.info("Click Logout")
                    self.lp.Click_Logout()
                    XLutils.writedata(self.path, 'Sheet1', r, 4, "Pass")
                else:
                    self.exp_status == "Fail"
                    login_status_list.append("Fail")
                    self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_ddt_004-Fail.png")
                    XLutils.writedata(self.path, 'Sheet1', r, 4, "Fail")
            else:
                if self.exp_status == "Pass":
                    login_status_list.append("Fail")
                    self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_ddt_004-Fail.png")
                    XLutils.writedata(self.path, 'Sheet1', r, 4, "Fail")
                else:
                    self.exp_status == "Fail"
                    login_status_list.append("Pass")
                    self.driver.save_screenshot("D:\\Pytest rev\\orangeHRM scratch\\Screenshots\\test_login_ddt_004-Pass.png")
                    XLutils.writedata(self.path, 'Sheet1', r, 4, "Fail")

            print(login_status_list)

        if "Pass" in login_status_list:
            self.log.info("test_login_ddt_004 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_004 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_ddt_004 is Completed")