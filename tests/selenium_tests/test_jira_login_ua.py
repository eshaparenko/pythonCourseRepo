import pytest

from tests.selenium_tests.base_test import BaseTest


@pytest.mark.ui
class TestLogin(BaseTest):

    def test_login_to_jira(self):
        self.login_page.open()
        self.login_page.at_page()
        self.login_page.enter_username("YevhenShaparenko")\
            .enter_password("YevhenShaparenko")\
            .click_login()
        self.home_page.at_page()

    def test_login_to_jira_with_wrong_username(self):
        self.login_page.open()
        self.login_page.at_page()
        self.login_page.enter_username("test")\
            .enter_password("YevhenShaparenko")\
            .click_login()
        self.login_page\
            .incorrect_username_message_shown()

    def test_login_to_jira_with_wrong_password(self):
        self.login_page.open()
        self.login_page.at_page()
        self.login_page.enter_username("YevhenShaparenko")\
            .enter_password("ewew")\
            .click_login()
        self.login_page\
            .incorrect_password_message_shown()


class TestCreateIssue(BaseTest):
    def test_create_issue_with_all_required_fields(self):
        self.login_page.login_to_jira("YevhenShaparenko", "YevhenShaparenko")
        self.home_page.create_issue()
        self.create_isssue_page.at_page()
        self.create_isssue_page\
            .set_summary()\
            .create()
        self.home_page.at_page()

