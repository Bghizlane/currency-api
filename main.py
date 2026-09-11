import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("CURRENCY_API_URL")


def convert_currency(from_currency, to_currency, amount):
    url = f"{API_URL}?from={from_currency}&to={to_currency}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            rate = data["rates"][to_currency]
            return amount * rate

        return None

    except requests.RequestException:
        return None