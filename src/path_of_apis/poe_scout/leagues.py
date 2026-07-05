from dataclasses import dataclass

import requests


@dataclass
class DefaultCurrency:
    ApiId: str
    Text: str
    IconUrl: str
    RelativePrice: float

@dataclass
class League:
    Value: str
    ShortName: str
    IsCurrent: bool
    DivinePrice: float
    ChaosDivinePrice: float
    BaseCurrencyApiId: str
    BaseCurrencyText: str
    BaseCurrencyIconUrl: str
    ExaltedCurrencyText: str
    ExaltedCurrencyIconUrl: str
    DivineCurrencyText: str
    DivineCurrencyIconUrl: str
    ChaosCurrencyText: str
    ChaosCurrencyIconUrl: str
    DefaultCurrency: DefaultCurrency

@dataclass
class ExchangeSnapshot:
    Epoch: int
    Volume: float
    MarketCap: float
    BaseCurrencyApiId: str
    BaseCurrencyText: str

@dataclass
class ReferenceCurrency:
    ApiId: str
    Text: str
    IconUrl: str
    RelativePrice: float

@dataclass
class SnapshotDataEntry:
    Epoch: int
    MarketCap: str
    Volume: str

@dataclass
class SnapshotHistory:
    Data: list[SnapshotDataEntry]
    Meta: dict
    BaseCurrencyApiId: str
    BaseCurrencyText: str

@dataclass
class Currency:
    CurrencyItemId: int
    ItemId: int
    CurrencyCategoryId: int
    ApiId: str
    Text: str
    CategoryApiId: str
    IconUrl: str
    ItemMetadata: dict | None

@dataclass
class CurrencyData:
    ValueTraded: str
    RelativePrice: str
    StockValue: str
    VolumeTraded: int
    HighestStock: int

@dataclass
class SnapshotPair:
    CurrencyExchangeSnapshotPairId: int
    CurrencyExchangeSnapshotId: int
    Volume: str
    BaseCurrencyApiId: str
    BaseCurrencyText: str
    CurrencyOne: Currency
    CurrencyTwo: Currency
    CurrencyOneData: CurrencyData
    CurrencyTwoData: CurrencyData


class Leagues:
    def __init__(self, base_url: str, sub_url: str = "/{}/Leagues", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout

    def get_leagues(self, realm: str) -> list[League]:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm), timeout=self.timeout)
            return [League(**value) for value in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e
    
    def get_exchange_snapshot(self, realm:str, league: str) -> ExchangeSnapshot:
        try:
            resp = requests.get(self.base_url +  self.sub_url.format(realm) + "/{}/ExchangeSnapshot".format(league), timeout=self.timeout)
            return ExchangeSnapshot(**resp.json())
        except requests.exceptions.RequestException as e:
            raise e
    
    def get_reference_currencies(self, realm: str, league: str) -> list[ReferenceCurrency]:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm) + "/{}/ReferenceCurrencies".format(league), timeout=self.timeout)
            return [ReferenceCurrency(**currency) for currency in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e
        
    def get_snapshot_history(self, realm: str, league: str, limit: int) -> SnapshotHistory:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm) + "/{}/SnapshotHistory".format(league), params={"Limit": limit}, timeout=self.timeout)
            return SnapshotHistory(**resp.json())
        except requests.exceptions.RequestException as e:
            raise e
        
    def get_snapshot_pairs(self, realm:str, league:str) -> list[SnapshotPair]:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm) + "/{}/SnapshotPairs".format(league), timeout=self.timeout)
            return [SnapshotPair(**pair) for pair in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e