import pytest

from tests.api.api_reaquests import login


@pytest.mark.api
class TestJiraRequests:

    @pytest.mark.parametrize('login_info', [
        {
            "username": "YevhenShaparenko",
            "password": "YevhenShaparenko"
        }])
    def test_login_positive(self, login_info):
        status_code = login(login_info)
        assert status_code == 200

    @pytest.mark.parametrize('login_info', [
        {
            "username": "YevhenShaparenko",
            "password": "blahblahblah"
        },
        {
            "username": "blahblahblah",
            "password": "YevhenShaparenko"
        }])
    def test_login_negative(self, login_info):
        status_code, response = login(login_info)
        assert status_code == 401

