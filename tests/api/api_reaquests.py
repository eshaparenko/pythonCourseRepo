import requests

from tests.api import configuration



def login(login_info):
    response = requests.post(configuration.PARAMS['base_url'] + configuration.ENDPOINTS['login_ep'], json=login_info)
    return response.status_code