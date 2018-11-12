import requests
import json

import sanitizers


def get_rate(currency):
    currency = sanitizers.currency(currency)
    url = 'https://openexchangerates.org/api/latest.json'\
          '?app_id=841a28ce9a464522bae12e9001d22ec8'

    raw_response = requests.get(url)
    loaded_response = json.loads(raw_response.text)
    rates = loaded_response['rates']
    if currency in rates:
        rate = rates[currency]
    else:
        raise ValueError("currency {} is not provided by the OER API".format(currency))
    return rate
