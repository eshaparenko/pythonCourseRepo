import allure
from selenium.webdriver.common.by import By

from selenium_project.pages.home_page import HomePage


class LoginPage():
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")
    USERNAME_ERROR_MESSAGE = (By.ID, "usernameerror")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Enter user name')
    def enter_username(self, username):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(username)
        return self

    @allure.step('Enter password')
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        return self

    @allure.step('Click login button')
    @allure.step('Login to Jira with user name and password')
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    def at_page(self):
        assert "System Dashboard - Hillel IT School JIRA" in self.driver.title

    @allure.step('Open Jira link')
    def open(self):
        self.driver.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        return self


    def login_to_jira(self, username, password):
        self.open()
        self.enter_username(username)\
            .enter_password(password)\
            .click_login()

    # @allure.attach.file("PNG attachment", name="Incorrect user name", attachment_type=allure.attachment_type.PNG)
    def incorrect_username_message_shown(self):
        assert "Sorry, your userid is required to answer a CAPTCHA question correctly." in self.driver.find_element(*self.USERNAME_ERROR_MESSAGE).text

    def incorrect_password_message_shown(self):
        assert "Sorry, your username and password are incorrect - please try again." in self.driver.find_element(*self.USERNAME_ERROR_MESSAGE).text