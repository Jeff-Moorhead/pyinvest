import os
import json


class Config:
    def __init__(self, configpath):
        self._data = self._get_config_data(configpath)
        self.refresh_token = self._data['refresh_token']
        self.client_id = self._data['client_id']
        self.account_id = self._data['account_id']

    def _get_refresh_token(self):
        return self.authentication_data['refresh_token']

    def _get_authentication_data(self):
        return {'refresh_token': self.data['refresh_token'], 'client_id': self.data['client_id']}

    def _get_account_id(self):
        return self.data['account_id']

    def _get_config_data(self, configpath):
        return json.load(open(os.path.expandvars(configpath)))

