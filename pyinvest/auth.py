"""
To authenticate, you need an access token. Access tokens last for thirty minutes.
When the access token expires, you need to use a refresh token to get a new one.

Authorization code URL: https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={localhost_encoded}&client_id={client_id}
Access code URL: https://api.tdameritrade.com/v1/oauth2/token
Form data: grant_type, refresh_token, client_id
"""

import requests


def authenticate(refresh_token, client_id):
    URL = 'https://api.tdameritrade.com/v1/oauth2/token'
    data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': client_id}
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(URL, headers=headers, data=data)

    response.raise_for_status()

    return response.json()['access_token']


"""
def get_new_refresh_token():
    "
    This will require automated web browser control
    "
    #AUTHENTICATION_URL = f'https://auth.tdameritrade.com/auth?response_type=code&redirect_uri={redirect}&client_id={client_id}%40AMER.OAUTHAP' # This brings you to the TDA login page. Figure out how to automate this login process. This will allow you to get refresh tokens automatically.
    response = requests.get(AUTHENTICATION_URL)
    response.raise_for_status()

    return response
"""

