import requests
from django.core.cache import cache

from Core.Utils.Enums import SupportedCurrency, ConvertCurrencyCode



class CurrencyConverter:
    def __init__(self):
        self.api_key = "b36d46c4a0446631eed00ff9ecf212cc"
        self.base_url = "http://data.fixer.io/api/latest?base=USD&access_key="

    def convert(self, amount: float, currency: str = None) -> float:
        if currency is None or currency.upper() == "USD":
            return amount

        rate = self.get_rate(currency.upper())
        new_amount = float(amount) / float(rate)
        return new_amount

    def get_rate(self, currency_code: str) -> float:
        cache_key = f"rate_{currency_code}"
        rate = cache.get(cache_key)
        if rate is None:
            url = f"{self.base_url}{self.api_key}&symbols={currency_code}"
            response = requests.get(url)
            data = response.json()
            rate = data['rates'][currency_code]
            cache.set(cache_key, rate, 60 * 15)  # кэширование на 15 минут
        return rate

# class CurrencyConverter:
#   def __init__(self):
#     self.base_url = "https://api.binance.com/api/v3/ticker/price?symbol="
#
#   def convert(self, amount: float, currency: str = None) -> float:
#     if currency is None or currency.upper() == SupportedCurrency.USD.value:
#       return amount
#
#     rate = self.get_rate(currency.upper())
#     if currency.upper() in [SupportedCurrency.RUB.value, SupportedCurrency.UAH.value]:
#       new_amount = float(amount) / float(rate)
#     else:
#       new_amount = float(amount) * float(rate)
#     return new_amount
#
#   def get_rate(self, currency_code: str) -> float:
#     cache_key = f"rate_{currency_code}"
#     rate = cache.get(cache_key)
#     if rate is None:
#       url = f"{self.base_url}{ConvertCurrencyCode[currency_code].value}"
#       rate = requests.get(url).json().get('price')
#       cache.set(cache_key, rate, 60 * 15)  # кэширование на 5 минут
#     return rate
