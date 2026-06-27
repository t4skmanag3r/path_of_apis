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



class Items:
    def __init__(self, base_url: str, sub_url: str = "/{}/Leagues/{}/Items", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout

    def get_items(self, realm: str, league: str):
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm, league), timeout=self.timeout)
            return [Item(**value) for value in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e
        
    def get_daily_stats_history(self, realm: str, league: str):
        try: 
            resp = requests.get(self.base_url + self.sub_url.format(realm, league), timeout=self.timeout)
            return DailyStatsHistory(**resp.json())
        except requests.exceptions.RequestException as e:
            raise e
