from selenium.webdriver.common.by import By

from selenium_project.pages.home_page import HomePage


class LoginPage():
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")
    USERNAME_ERROR_MESSAGE = (By.ID, "usernameerror")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    def at_page(self):
        assert "System Dashboard - Hillel IT School JIRA" in self.driver.title

    def open(self):
        self.driver.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        return self

    def login_to_jira(self, username, password):
        self.open()
        self.enter_username(username)\
            .enter_password(password)\
            .click_login()

    def incorrect_username_message_shown(self):
        assert "Sorry, your userid is required to answer a CAPTCHA question correctly." in self.driver.find_element(*self.USERNAME_ERROR_MESSAGE).text

    def incorrect_password_message_shown(self):
        assert "Sorry, your username and password are incorrect - please try again." in self.driver.find_element(*self.USERNAME_ERROR_MESSAGE).text