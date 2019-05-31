from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium_project.pages.create_issue_page import CreateIssuePage
from selenium_project.pages.home_page import HomePage
from selenium_project.pages.login_page import LoginPage


class BaseTest:
    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.create_isssue_page = CreateIssuePage(self.driver)

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()