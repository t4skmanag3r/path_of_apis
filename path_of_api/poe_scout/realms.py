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

class Realms:
    def __init__(self, base_url: str, sub_url: str = "/Realms", timeout = 100):
        self.base_url = base_url
        self.sub_url = sub_url
        self.timeout = timeout

    def get_realms(self):
        try:
            resp = requests.get(self.base_url + self.sub_url, timeout=self.timeout)
            return [Realm(**value) for value in resp.json()]
        except requests.exceptions.RequestException as e:
            raise e
