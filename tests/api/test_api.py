import pytest

from tests.api.api_reaquests import login, create_issue, delete_issue


@pytest.mark.api
class TestJiraRequests:

    @pytest.mark.parametrize('login_info', [
        {
            "username": "YevhenShaparenko",
            "password": "YevhenShaparenko"
        }])
    def test_login_positive(self, login_info):
        response = login(login_info)
        assert response.status_code == 200

    @pytest.mark.parametrize('login_info', [
        {
            "username": "YevhenShaparenko",
            "password": "blahblahblah"
        }])
    def test_login_negative(self, login_info):
        response = login(login_info)
        assert response.status_code == 401

    @pytest.mark.parametrize('issue', [
        {
            "fields": {
                "project":
                    {
                        "key": "WEBINAR"
                    },
                "summary": "Test create issue via api",
                "description": "Test create issue via api",
                "issuetype": {
                    "name": "Bug"
                }
            }
        }])
    def test_create_issue_positive(self, issue):
        response = create_issue(issue)
        assert response.status_code == 201

        new_key = response.json()['key']
        delete_response = delete_issue(new_key)
        assert delete_response.status_code == 204

    @pytest.mark.parametrize('issue', [
        {
            "fields": {
                "project":
                    {
                        "key": "WEBINAR"
                    },
                "summary": "Test create issue via api",
                "description": "Test create issue via api",
                "issuetype": {
                    "name": ""
                }
            }
        }])
    def test_create_issue_negative(self, issue):
        response = create_issue(issue)
        assert response.status_code == 400