import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    PAGE_LOCATOR = (By.ID, "header-details-user-fullname")

    def __init__(self, driver):
        self.driver = driver

    def at_page(self):
        profile_logo_element = WebDriverWait(self.driver, 10)\
            .until(EC.presence_of_element_located((By.ID, "header-details-user-fullname")))
        assert profile_logo_element.is_displayed()

    def create_issue(self):
        time.sleep(3)
        self.driver.execute_script("document.getElementById('create_link').click()")
        return self


