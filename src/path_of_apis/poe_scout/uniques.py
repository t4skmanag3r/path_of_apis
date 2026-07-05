from dataclasses import dataclass

import requests


@dataclass
class PriceLog:
    Price: float
    Time: str
    Quantity: int

@dataclass
class UniqueItem:
    UniqueItemId: int
    ItemId: int
    IconUrl: str
    Text: str
    Name: str
    CategoryApiId: str
    ItemMetadata: dict
    Type: str
    IsChanceable: bool
    PriceLogs: list[PriceLog]
    CurrentPrice: float
    CurrentQuantity: int


@dataclass
class CategoryResponse:
    CurrentPage: int
    Pages: int
    Total: int
    Items: list[UniqueItem]


class Uniques:
    def __init__(self, base_url: str, sub_url: str = "/{}/Leagues/{}/Uniques", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout

    def get_category_items(self, realm: str, league: str, category: str) -> CategoryResponse:
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm, league) + "/ByCategory", params={"Category": category}, timeout=self.timeout)
            return CategoryResponse(**resp.json())
        except Exception as e:
            raise e