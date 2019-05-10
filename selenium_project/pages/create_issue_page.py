import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_project.pages.base_page import BasePage


class CreateIssuePage(BasePage):
    SUMMARY = (By.ID, 'summary')
    ISSUE_TYPE_INPUT = (By.ID, 'issuetype-field')
    ISSUE_TYPE = (By.XPATH, "//*[@id='issuetype-field' and contains(@aria-activedescendant, 'bug')]")

    def __init__(self, driver):
        super().__init__(driver)

    def at_page(self):
        create_issue_page_locator = self.wait_for_element_visible((By.XPATH, "//h2[@title='Create Issue']"), 10)
        assert create_issue_page_locator.is_displayed()

    def set_summary(self):
        summary: WebElement = self.driver.find_element(*self.SUMMARY)
        summary.clear()
        summary.send_keys("AQA_PYTHON_TEST")
        return self

    def set_issue_type(self):
        issue_type: WebElement = self.driver.find_element(*self.ISSUE_TYPE_INPUT)
        issue_type.click()
        issue = self.driver.find_element_by_tag_name(*self.ISSUE_TYPE)
        issue.click()
        return self

    def create(self):
        create_button: WebElement = self.driver.find_element(By.ID, "create-issue-submit")
        create_button.click()
        time.sleep(1)
        return self