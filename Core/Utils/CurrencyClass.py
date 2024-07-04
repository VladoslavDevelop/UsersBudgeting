import os
import django
from _decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CryptoWallet.settings')
django.setup()

import requests
from django.core.cache import cache



# class CurrencyClass:
#   @staticmethod
#   def convert(currency: str, amount: float, to_usd: bool = True) -> float:
#     cache_key = f"rate_{currency}"
#     rate_data = cache.get(cache_key)
#
#     if rate_data is None:
#       currency_usd = Currency.objects.get(code='USD')
#       currency_out = Currency.objects.get(code=currency)
#       currency_t = CurrencyRate.objects.get(name=currency_usd, name2=currency_out)
#       rate_data = Decimal(currency_t.k)
#       cache.set(cache_key, rate_data, 60 * 15)  # кэширование на 5 минут
#
#     if currency == 'TRX' and not to_usd:
#       return round(Decimal(amount) * rate_data, 6)
#
#     if to_usd:
#       amount_out = Decimal(amount) * rate_data
#     else:
#       amount_out = Decimal(amount) / rate_data
#
#     return round(amount_out, 2 if to_usd else 6)


class CurrencyClass:
    @staticmethod
    def convert(currency: str, amount: float, to_usd: bool = True) -> float:
        cache_key = f"rate_{currency}"
        rate_data = cache.get(cache_key)
        if rate_data is None:
            try:
                response = requests.get(
                    f"https://api.binance.com/api/v3/ticker/price?symbol={currency.upper()}USDT"
                )
                price = response.json().get('price')
                balance_usd = float(amount) * float(price)
                cache.set(cache_key, price, 60 * 15)
            except requests.exceptions.RequestException as e:
                print(f"Error during Binance API request: {e}")
                return 0
        else:
            price = rate_data
            balance_usd = float(amount) * float(price)

        return balance_usd



