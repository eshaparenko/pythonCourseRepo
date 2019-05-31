import requests

from tests.api import configuration



def login(login_info):
    response = requests.post(configuration.PARAMS['base_url'] + configuration.ENDPOINTS['login_ep'], json=login_info)
    return response.status_code


def create_issue(issue):
    response = requests.post(configuration.PARAMS['base_url'] + configuration.ENDPOINTS['issue_ep'], json=issue,
                             auth=(configuration.PARAMS['login'], configuration.PARAMS['password']))
    return response.status_code, response.json()