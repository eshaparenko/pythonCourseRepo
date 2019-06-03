import requests

from tests.api import configuration



def login(login_info):
    response = requests.post(configuration.PARAMS['base_url'] + configuration.ENDPOINTS['login_ep'], json=login_info)
    return response


def create_issue(issue):
    response = requests.post(configuration.PARAMS['base_url'] + configuration.ENDPOINTS['issue_ep'], json=issue,
                             auth=(configuration.PARAMS['login'], configuration.PARAMS['password']))
    return response

def delete_issue(key):
    response = requests.delete(configuration.PARAMS['base_url'] + configuration.ENDPOINTS['issue_ep'] + '/' + key,
                               auth=(configuration.PARAMS['login'], configuration.PARAMS['password']))
    return response