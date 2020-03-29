import requests
from pyinvest import auth

"""
Significant keys: positions, unsettledCash, cashAvailableForTrading
"""


def get_account_info(account, access_token):
    URL = f"https://api.tdameritrade.com/v1/accounts/{account}"
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'fields': 'positions'}
    response = requests.get(URL, headers=headers, params=params)
    
    response.raise_for_status()

    return response.json()['securitiesAccount']


def get_positions(account, access_token):
    return get_account_info(account, access_token)['positions']

