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


class Leagues:
    def __init__(self, base_url: str, sub_url: str = "/{}/Leagues", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout

    def get_leagues(self, realm: str):
        try:
            resp = requests.get(self.base_url + self.sub_url.format(realm), timeout=self.timeout)
            return [League(**value) for value in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e
    
