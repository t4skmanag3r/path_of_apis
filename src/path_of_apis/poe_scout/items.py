from dataclasses import dataclass

import requests


@dataclass
class Item:
    ItemId: int
    CategoryApiId: str
    Text: str
    Name: str
    Type: str
    ApiId: int | None
    CurrentPrice: float
    IconUrl: str

@dataclass
class DailyStats:
    Time: str
    Open: int
    High: int
    Low: int
    Close: int
    Average: float
    Volume : int

@dataclass
class DailyStatsHistory:
    DailyStats: DailyStats
    HasMore: bool
    BaseCurrencyApiId: str
    BaseCurrencyText: str

@dataclass
class Category:
    ApiId: str
    Label: str
    Icon: str

@dataclass
class UniqueCategory(Category):
    ItemCategoryId: int

@dataclass
class CurrencyCategory(Category):
    CurrencyCategoryId: int


@dataclass
class CategoriesResponse:
    UniqueCategories: list[UniqueCategory]
    CurrencyCategories: list[CurrencyCategory]

@dataclass
class PriceHistoryEntry:
    Price: str
    Time: str
    Quantity: int

@dataclass
class ItemPriceHistory:
    ItemId: int
    History: list[PriceHistoryEntry]

class Items:
    def __init__(self, base_url: str, sub_url: str = "/{}/Leagues/{}/Items", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout

    def get_items(self, realm: str, league: str) -> list[Item]:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm, league), timeout=self.timeout)
            return [Item(**value) for value in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e
        
    def get_daily_stats_history(self, realm: str, league: str) -> DailyStatsHistory:
        try: 
            resp = requests.get(self.base_url + self.sub_url.format(realm, league), timeout=self.timeout)
            return DailyStatsHistory(**resp.json())
        except requests.exceptions.RequestException as e:
            raise e

    def get_categories(self, realm: str, league: str) -> CategoriesResponse:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm, league) + "/Categories", timeout=self.timeout)
            data = resp.json()
            return CategoriesResponse(
                UniqueCategories=[UniqueCategory(**item) for item in data["UniqueCategories"]],
                CurrencyCategories=[CurrencyCategory(**item) for item in data["CurrencyCategories"]]
            )
        except requests.exceptions.RequestException as e:
            raise e
        
    def get_price_history(self, realm: str, league:str) -> list[ItemPriceHistory]:
        try:
            resp = requests.get(url=self.base_url + self.sub_url.format(realm, league) + "/PriceHistory", timeout=self.timeout)
            data = resp.json()
            return [ItemPriceHistory(**item) for item in data["ItemHistories"]]
        except requests.exceptions.RequestException as e:
            raise e
        
    def get_item(self, realm: str, league: str, item_id: int) -> Item:
        try:
            resp = requests.get(url=self.base_url + self.sub_url.format(realm, league) + "/Item/" + str(item_id), timeout=self.timeout)
            data = resp.json()
            return Item(**data["Item"])
        except requests.exceptions.RequestException as e:
            raise e
        
    def get_item_history(self, realm: str, league: str, item_id: int, log_count: int) -> list[PriceHistoryEntry]:
        if log_count % 4 != 0:
            raise ValueError("Log count must be a multiple of 4")
        try:
            resp = requests.get(url=self.base_url + self.sub_url.format(realm, league) + "/" + str(item_id) + "/History/", params={"LogCount": log_count},  timeout=self.timeout)
            data = resp.json()
            print(data)
            return [PriceHistoryEntry(**entry) for entry in data["PriceHistory"]]
        except requests.exceptions.RequestException as e:
            raise e