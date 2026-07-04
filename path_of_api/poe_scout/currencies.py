

from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class PriceLog:
    Price: float
    Time: str
    Quantity: int

@dataclass
class Currency:
    CurrencyItemId: int
    ItemId: int
    CurrencyCategoryId: int
    ApiId: str
    Text: str
    CategoryApiId: str
    IconUrl: str
    PriceLogs: list[PriceLog]
    ItemMetadata: Optional[dict]
    CurrentPrice: float

@dataclass
class CategoryResponse:
    CurrentPage: int
    Pages: int
    Total: int
    Items: list[Currency]

@dataclass
class CurrencyStats:
    CurrencyItemId: int
    ValueTraded: str
    RelativePrice: str
    StockValue: str
    VolumeTraded: int
    HighestStock: int

@dataclass
class CurrencyData:
    CurrencyOneData: CurrencyStats
    CurrencyTwoData: CurrencyStats

@dataclass
class CurrencyPairHistory:
    Epoch: int
    Data: CurrencyData
    

@dataclass
class CurrencyPairResponse:
    History: list[CurrencyPairHistory]
    Meta: dict
    BaseCurrencyApiId: str
    BaseCurrencyText: str


class Currencies:
    def __init__(self, base_url: str, sub_url: str = "/{}/Leagues/{}/Currencies", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout
    
    def get_currency(self, realm: str, league: str, apiid: str) -> Currency:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm, league) + f"/{apiid}", timeout=self.timeout)
            return Currency(**resp.json())
        except Exception as e:
            raise e
        
    def get_by_category(self, realm:str, league:str, category: str) -> CategoryResponse:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm, league) + "/ByCategory", params={"Category": category}, timeout=self.timeout)
            return CategoryResponse(**resp.json())
        except Exception as e:
            raise e
        
    def get_pair_history(self, realm:str, league:str, currency1_id: int, currency2_id: int, limit: int) -> CurrencyPairResponse:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm, league) + "/Pairs/{}/{}/History".format(currency1_id, currency2_id), params={"Limit": limit}, timeout=self.timeout)
            return CurrencyPairResponse(**resp.json())
        except Exception as e:
            raise e