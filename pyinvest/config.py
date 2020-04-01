import os
import json


class Config:
    def __init__(self, configpath):
        self._data = self._get_config_data(configpath)
        self.refresh_token = self._data['refresh_token']
        self.client_id = self._data['client_id']
        self.account_id = self._data['account_id']

    def _get_config_data(self, configpath):
        return json.load(open(os.path.expandvars(configpath)))

