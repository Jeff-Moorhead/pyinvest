import os
import json


class Config:
    def __init__(self, configpath):
        self._data = self._get_config_data(configpath)
        self.client_id = self._data['client_id']
        self.username = self._data['username']
        self.account_id = self._data['account_id']
        self.redirect = self._data['redirect']
        self.allocations = self._data['allocations']

    def _get_config_data(self, configpath):
        return json.load(open(os.path.expandvars(configpath)))

