import requests
import json

import sanitizers as sani


def get_rate(currency):
    currency = sani.currency(currency)
    url = 'https://openexchangerates.org/api/latest.json'\
          '?app_id=841a28ce9a464522bae12e9001d22ec8'

    raw_response = requests.get(url)
    loaded_response = json.loads(raw_response.text)
    rates = loaded_response['rates']
    rate = rates[currency]
    return rate
