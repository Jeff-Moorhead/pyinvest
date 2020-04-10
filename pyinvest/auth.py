"""
To authenticate, you need an access token. Access tokens last for thirty minutes.
When the access token expires, you need to use a refresh token to get a new one.

Authorization code URL: https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={localhost_encoded}&client_id={client_id}
Access code URL: https://api.tdameritrade.com/v1/oauth2/token
Form data: grant_type, refresh_token, client_id
"""

import requests
import urllib.parse as up

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import ui


def authenticate(client_id, redirect, username, password):
    auth_code = _get_auth_code(client_id, redirect, username, password) 
    api_endpoint = 'https://api.tdameritrade.com/v1/oauth2/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'authorization_code',
        'refresh_token': '',
        'access_type': 'offline',
        'code': auth_code,
        'client_id': client_id,
        'redirect_uri': redirect
        }
    response = requests.post(api_endpoint, data=data, headers=headers)
    return response.json()['access_token']


def _get_auth_code(client_id, redirect, username, password):
    client_id += '@AMER.OAUTHAP'
    encoded_redirect = up.quote(redirect)
    encoded_client_id = up.quote(client_id)
    url = f'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={encoded_redirect}&client_id={encoded_client_id}'

    driver = webdriver.Firefox()     
    driver.get(url)

    wait = ui.WebDriverWait(driver, 60)

    ubox = driver.find_element('id', 'username')
    pbox = driver.find_element('id', 'password')
    ubox.send_keys(username)
    pbox.send_keys(password)
    driver.find_element('id', 'accept').click()
    driver.find_element('id', 'accept').click()
    code = driver.find_element('id', 'smscode')
    code.click()
    wait.until(lambda driver: len(code.get_attribute('value')) == 6)
    driver.find_element('id', 'accept').click()

    try:
        driver.find_element('id', 'accept').click()
    except WebDriverException:
        # This is kind of hacky. I think this exception is cause by a bug in Selenium.
        # Catching the exception prevents the program from exiting.
        pass

    while True:
        try:
            authentication_code = driver.current_url.split('code=')[1]
            decoded_code = up.unquote(authentication_code)
            if decoded_code:
                break
            else:
                sleep(2)
        except (TypeError, IndexError):
            continue

    driver.close()
        
    return decoded_code
 
