from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By


class loginpage:
    Text_username_XPATH = (By.XPATH, "//input[@placeholder='Username']")
    Text_password_XPATH = (By.XPATH, "//input[@placeholder='Password']")
    Click_login_XPATH = (By.XPATH, "//button[@type='submit']")
    Click_Menu_Button_XPATH = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_Button_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*loginpage.Text_username_XPATH).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*loginpage.Text_password_XPATH).send_keys(password)

    def Click_login(self):
        self.driver.find_element(*loginpage.Click_login_XPATH).click()

    def Click_MenuButton(self):
        self.driver.find_element(*loginpage.Click_Menu_Button_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*loginpage.Click_Logout_Button_XPATH).click()

    def login_status(self):
        try:
            self.driver.find_element(*loginpage.Click_Menu_Button_XPATH)
            return True
        except Ec:
            return False
