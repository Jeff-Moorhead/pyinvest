import requests

"""
Significant keys: positions, unsettledCash, cashAvailableForTrading

This would be better to refactor into a class. Look into the requests.Session class.
"""


def calculate_total_profit(shares, avg_cost, current_price):
    return round((current_price - avg_cost) * shares, 2)


def calculate_total_profit_percentage(shares, avg_cost, current_price):
    pcnt = ((shares * current_price) - (shares * avg_cost)) / (shares * avg_cost)
    return round(pcnt * 100, 2)


class TDAmeritradeClient:
    def __init__(self, access_token, account):
        self.account = account
        self.session = requests.Session()
        self.session.headers = {'Authorization': f'Bearer {access_token}'}

    def get_account_info(self):
        URL = f"https://api.tdameritrade.com/v1/accounts/{self.account}"
        params = {'fields': 'positions'}

        response = self.session.get(URL, params=params) 
        response.raise_for_status()
        return response.json()['securitiesAccount']

    def get_positions(self):
        return self.get_account_info()['positions']

    def place_order(self, symbol, quantity):
        URL = f"https://api.tdameritrade.com/v1/accounts/{self.account}/orders"
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
        response = self.session.post(URL, json=params)
        return response.status_code

    def cancel_order(self, orderid):
        URL = f"https://api.tdameritrade.com/v1/accounts/{account}/orders/{orderid}"
        response = self.session.delete(URL)
        return response.status_code

    def get_orders(self):
        URL = f"https://api.tdameritrade.com/v1/accounts/{account}/orders"
        response = self.session.get(URL)
        response.raise_for_status()
        return response.json()

