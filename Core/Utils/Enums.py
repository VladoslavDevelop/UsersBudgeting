from enum import Enum


class StatusInvoice(Enum):
  CREATED = 'created'
  PAID = 'paid'
  FAILED = 'failed'
  CANCELED = 'canceled'
  PARTIAL = 'partial'
  EXCHANGE = 'exchange'
  OVERPAID = 'overpaid'


class TypesInvoice(Enum):
  UP = 'up'
  DW = 'dw'
  CHANGE = 'change'
  DEMO = 'demo'


class SupportedCurrency(Enum):
  RUB = 'RUB'
  UAH = 'UAH'
  USD = 'USD'
  EUR = 'EUR'
  GBP = 'GBP'


class CurrencyAddressFunction(Enum):
  BTC = 'GeneratedBTCAddress'
  LTC = 'GeneratedLTCAddress'
  ETH = 'GeneratedETHAddress'
  USDT = 'GeneratedUSDTAddress'


class ConvertCurrencyCode(Enum):
  RUB = 'USDTRUB'
  UAH = 'USDTUAH'
  EUR = 'EURUSDT'
  GBP = 'GBPUSDT'


class ConvertCurrencyCryptoCode(Enum):
  BTCLTC = 'LTCBTC_division'
  BTCETH = 'ETHBTC_division'
  BTCUSDT = 'BTCUSDT_multi'
  LTCBTC = 'LTCBTC_multi'
  LTCETH = 'LTCETH_multi'
  LTCUSDT = 'LTCUSDT_multi'
  ETHBTC = 'ETHBTC_multi'
  ETHLTC = 'LTCETH_division'
  ETHUSDT = 'ETHUSDT_multi'
  USDTBTC = 'BTCUSDT_division'
  USDTLTC = 'LTCUSDT_division'
  USDTETH = 'ETHUSDT_division'


class PairExchange(Enum):
  BTCLTC = 'btc_ltc'
  BTCETH = 'btc_eth'
  BTCUSDT = 'btc_usdttrc20'
  LTCBTC = 'ltc_btc'
  LTCETH = 'ltc_eth'
  LTCUSDT = 'ltc_usdttrc20'
  ETHBTC = 'eth_btc'
  ETHLTC = 'eth_ltc'
  ETHUSDT = 'eth_usdttrc20'
  USDTBTC = 'usdttrc20_btc'
  USDTLTC = 'usdttrc20_ltc'
  USDTETH = 'usdttrc20_eth'