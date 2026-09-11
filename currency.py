import requests


def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][to_currency]
        result = amount * rate

        return result

    return None