from dataclasses import dataclass

import requests


@dataclass
class Realm:
    value: str
    label: str
    game_api_id: str
    realm_api_id: str
    trade_api_path: str
    default_league_value: str

@dataclass
class Filter:
    DisplayName: str
    Category: str
    Identifier: str
    ItemKind: str

@dataclass
class Item:
    CurrencyItemId: int
    ItemId: int
    CurrencyCategoryId: int
    ApiId: str
    Text: str
    CategoryApiId: str
    IconUrl: str
    ItemMetadata: object
    PriceLogs: list[object]
    CurrentPrice: object


class Realms:
    def __init__(self, base_url: str, sub_url: str = "/Realms", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout

    def get_realms(self) -> list[Realm]:
        try:
            resp = requests.get(self.base_url + self.sub_url, timeout=self.timeout)
            return [Realm(**value) for value in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e

    def get_filters(self, realm: str) -> list[Filter]:
        try:
            resp = requests.get(self.base_url + self.sub_url + "/{}/Filters".format(realm), timeout=self.timeout)
            return [Filter(**value) for value in resp.json()["Filters"]]
        except requests.exceptions.RequestException as e:
            raise e
    
    def get_landing_splash_info(self, realm: str) -> list[Item]:
        try:
            resp = requests.get(self.base_url + self.sub_url + "/{}/LandingSplashInfo".format(realm), timeout=self.timeout)
            return [Item(**value) for value in resp.json()["Items"]]
        except requests.exceptions.RequestException as e:
            raise e