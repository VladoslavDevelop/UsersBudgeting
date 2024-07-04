from _decimal import Decimal

from Currency.models import Currency, CurrencyRate


class RateFiatCrypto:
  def __init__(self, currency: Currency, crypto: bool):
    self.currency = currency
    self.rate = self.get_rate()

  def convert(self, amount: float, to_crypto: bool) -> Decimal:
    factor = self.rate if (to_crypto != (self.currency.code == 'USDT')) else 1 / self.rate
    return Decimal(amount) * Decimal(factor)

  def get_rate(self) -> float:
    currency_base = Currency.objects.get(code='USD')
    rate = CurrencyRate.objects.get(name=currency_base, name2=self.currency)
    return rate.k
