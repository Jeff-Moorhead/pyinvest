import os
import json


def get_authentication_data(configpath):
    data = _get_config_data(configpath)
    return {'refresh_token': data['refresh_token'], 'client_id': data['client_id']}


def get_account_data(configpath):
    data = _get_config_data(configpath)
    return {'account_id': data['account_id']}


def _get_config_data(configpath):
    return json.load(open(os.path.expandvars(configpath)))

