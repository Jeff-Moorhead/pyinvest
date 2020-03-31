import requests
from pyinvest import auth

"""
Significant keys: positions, unsettledCash, cashAvailableForTrading

This would be better to refactor into a class. Look into the requests.Session class.
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


def place_order(symbol, quantity, account, access_token):
    URL = f"https://api.tdameritrade.com/v1/accounts/{account}/orders"
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {
        "orderType": "MARKET",
        "session": "NORMAL",
        "duration": "DAY",
        "orderStrategyType": "SINGLE",
        "orderLegCollection": [
            {
                "instruction": "Buy",
                "quantity": quantity,
                "instrument": {
                    "symbol": f"{symbol}",
                    "assetType": "EQUITY"
                }
            }
        ]
    }
    response = requests.post(URL, headers=headers, json=params)

    return response.status_code


def cancel_order(orderid, account, access_token):
    URL = f"https://api.tdameritrade.com/v1/accounts/{account}/orders/{orderid}"
    headers = {'Authorization': f'Bearer {access_token}'} 
    response = requests.delete(URL, headers=headers)

    return response.status_code
 

def get_orders(account, access_token):
    URL = f"https://api.tdameritrade.com/v1/accounts/{account}/orders"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    
    return response.json()

